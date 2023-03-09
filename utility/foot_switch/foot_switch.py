import time
from talon import Module, Context, actions, ctrl, cron

mod = Module()

settings_timeout = mod.setting(
    "foot_switch_timeout",
    type=bool,
    default=True,
    desc="If true timeout will be used to decide if the foot switch was held or not",
)

# Obviously must match the talon file
TOP=0
CENTER=1
LEFT=2
RIGHT=3

current_state = [False, False, False, False]
last_state = [False, False, False, False]
pressed_for = [0, 0, 0, 0]
timestamps = [0, 0, 0, 0]
scroll_reversed = False
hold_timeout = 0.2
drag_threshold = 0.2

def on_interval():
    for key in range(4):
        if current_state[key] != last_state[key]:
            last_state[key] = current_state[key]
            # Key is pressed down
            if current_state[key]:
                call_down(key)
            # Key is released after specified hold time out. ie key was held.
            elif (
                not settings_timeout.get()
                or time.perf_counter() - timestamps[key] > hold_timeout
                or ( timestamps[key] != 0 and current_state[key] == False )
            ):
                call_up(key)


# In a hotkey down event, eg "key(ctrl:down)", any key you press with key/insert
# actions will be combined with ctrl since it's still held. Just updating a
# boolean in the actual hotkey event and reading it asynchronously with cron
# gets around this issue.
cron.interval("16ms", on_interval)
#print("foot switch timeout: {}".format( 'true' if settings_timeout.get() else 'false'))

def call_down(key: int):
    #print("call down {}".format(key))
    if key == TOP:
        actions.user.foot_switch_top_down()
    elif key == CENTER:
        actions.user.foot_switch_center_down()
    elif key == LEFT:
        actions.user.foot_switch_left_down()
    elif key == RIGHT:
        actions.user.foot_switch_right_down()

def call_up(key: int):
    #print("call up {}".format(key))
    if key == TOP:
        actions.user.foot_switch_top_up()
    elif key == CENTER:
        actions.user.foot_switch_center_up()
    elif key == LEFT:
        actions.user.foot_switch_left_up()
    elif key == RIGHT:
        actions.user.foot_switch_right_up()

@mod.action_class
class Actions:
    def foot_switch_down(key: int):
        """Foot switch key down event. Top(0), Center(1), Left(2), Right(3)"""
        timestamps[key] = time.perf_counter()
        current_state[key] = True

    def foot_switch_repeat(key: int):
        """Foot switch key repeat event. Top(0), Center(1), Left(2), Right(3)"""
        pressed_for[key] = time.perf_counter() - timestamps[key]

    def foot_switch_up(key: int):
        """Foot switch key up event. Top(0), Center(1), Left(2), Right(3)"""
        pressed_for[key] = time.perf_counter() - timestamps[key]
        current_state[key] = False
        #print( "Foot switch {} released after {:.3f}s".format( key, pressed_for[key] ))


    def foot_switch_scroll_reverse():
        """Reverse scroll direction using foot switch"""
        global scroll_reversed
        scroll_reversed = not scroll_reversed

    def foot_switch_top_down():
        """Foot switch button top:down"""

    def foot_switch_top_up():
        """Foot switch button top:up"""

    def foot_switch_center_down():
        """Foot switch button center:down"""

    def foot_switch_center_up():
        """Foot switch button center:up"""

    def foot_switch_left_down():
        """Foot switch button left:down"""

    def foot_switch_left_up():
        """Foot switch button left:up"""

    def foot_switch_right_down():
        """Foot switch button right:down"""

    def foot_switch_right_up():
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

    def foot_switch_top_up():
        actions.user.mouse_scroll_stop()

    def foot_switch_center_down():
        if scroll_reversed:
            actions.user.mouse_scrolling("up")
        else:
            actions.user.mouse_scrolling("down")

    def foot_switch_center_up():
        actions.user.mouse_scroll_stop()

    def foot_switch_left_down():
        actions.user.mouse_drag(0)

    def foot_switch_left_up():
        actions.user.mouse_drag_end()

    def foot_switch_right_down():
        actions.mouse_click(1)

    def foot_switch_right_up():
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

    def foot_switch_right_up():
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

    def foot_switch_left_up():
        actions.user.mute_microphone()
