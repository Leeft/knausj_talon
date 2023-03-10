import time
from talon import Module, Context, actions, cron
from .cron_driven_switch import CronDrivenSwitch

mod = Module()

TOP=0
CENTER=1
LEFT=2
RIGHT=3

scroll_reversed = False

switches = {
    TOP : CronDrivenSwitch( TOP, actions.user.foot_switch_top_down, actions.user.foot_switch_top_up ),
    CENTER : CronDrivenSwitch( CENTER, actions.user.foot_switch_center_down, actions.user.foot_switch_center_up ),
    LEFT : CronDrivenSwitch( LEFT, actions.user.foot_switch_left_down, actions.user.foot_switch_left_up ),
    RIGHT : CronDrivenSwitch( RIGHT, actions.user.foot_switch_right_down, actions.user.foot_switch_right_up )
}

@mod.action_class
class Actions:
    def track_foot_switch_down(key: int):
        """Track state of foot switch on down (press) event. Top(0), Center(1), Left(2), Right(3)"""
        switches[key].down()

    def track_foot_switch_up(key: int):
        """Record foot switch key up (release) event. Top(0), Center(1), Left(2), Right(3)"""
        switches[key].up()


    def foot_switch_scroll_reverse():
        """Reverse scroll direction using foot switch"""
        global scroll_reversed
        scroll_reversed = not scroll_reversed

    def foot_switch_top_down():
        """Foot switch button top:down"""

    def foot_switch_top_up(held: bool):
        """Foot switch button top:up"""

    def foot_switch_center_down():
        """Foot switch button center:down"""

    def foot_switch_center_up(held: bool):
        """Foot switch button center:up"""

    def foot_switch_left_down():
        """Foot switch button left:down"""

    def foot_switch_left_up(held: bool):
        """Foot switch button left:up"""

    def foot_switch_right_down():
        """Foot switch button right:down"""

    def foot_switch_right_up(held: bool):
        """Foot switch button right:up"""


# ---------- Default implementation ----------
ctx = Context()


@ctx.action_class("user")
class UserActions:
    def foot_switch_top_down():
        if scroll_reversed:
            actions.user.mouse_scrolling("down")
        else:
            actions.user.mouse_scrolling("up")

    def foot_switch_top_up(held: bool):
        actions.user.mouse_scroll_stop()

    def foot_switch_center_down():
        if scroll_reversed:
            actions.user.mouse_scrolling("up")
        else:
            actions.user.mouse_scrolling("down")

    def foot_switch_center_up(held: bool):
        actions.user.mouse_scroll_stop()

    def foot_switch_left_down():
        actions.user.mouse_drag(0)

    def foot_switch_left_up(held: bool):
        actions.user.mouse_drag_end()

    def foot_switch_right_down():
        actions.mouse_click(1)

    def foot_switch_right_up(held: bool):
        actions.mouse_release(1)


# ---------- Default non-sleep implementation ----------
ctx_eye_tracker = Context()
ctx_eye_tracker.matches = r"""
tag: user.eye_tracker
tag: user.eye_tracker_frozen
"""


@ctx_eye_tracker.action_class("user")
class NonSleepActions:
    def foot_switch_right_down():
        actions.user.mouse_freeze_toggle()

    def foot_switch_right_up(held: bool):
        actions.user.mouse_freeze_toggle()


# ---------- Audio conferencing ----------
ctx_voip = Context()
ctx_voip.matches = r"""
mode: command
mode: dictation
mode: sleep
tag: user.voip
"""


@ctx_voip.action_class("user")
class VoipActions:
    def foot_switch_left_down():
        actions.user.mute_microphone()

    def foot_switch_left_up(held: bool):
        actions.user.mute_microphone()
