import time
from talon import cron
from enum import Enum

# Global to keep track of the switches that have been created so that
# they can be enumerated over in the cron handling loop (calling code
# will probably also keep a copy; that's fine)
cron_driven_switches = {}

class CronDrivenSwitchState(Enum):
    NONE = 0
    DOWN = 1
    HELD = 2 # TODO
    UP   = 3

class CronDrivenSwitch:
    """State for a foot pedal switch (could be any key, but need to start somewhere).

    In a hotkey down event, eg "key(ctrl:down)", any key you press with key/insert
    actions will be combined with ctrl since it's still held. Just updating a
    boolean in the actual hotkey event and reading it asynchronously with cron
    gets around this issue."""

    def __init__(self, key, down_cb, up_cb, hold_timeout=0.2) -> None:
        global cron_driven_switches
        self.timestamp = 0
        self.event = CronDrivenSwitchState.NONE
        self.down_cb = down_cb
        self.up_cb = up_cb
        self.hold_timeout = hold_timeout
        cron_driven_switches[key] = self

    def check(self):
        if self.event == CronDrivenSwitchState.NONE:
            return

        event = self.event
        self.event = CronDrivenSwitchState.NONE

        if event == CronDrivenSwitchState.DOWN:
            self.down_cb()
        else:
            held = time.perf_counter() - self.timestamp > self.hold_timeout
            self.up_cb(held)

    def down(self):
        self.timestamp = time.perf_counter()
        self.event = CronDrivenSwitchState.DOWN

    def up(self):
        self.event = CronDrivenSwitchState.UP


def __on_interval():
    for key, switch in cron_driven_switches.items():
        switch.check()

cron.interval("16ms", __on_interval)

# EOF
