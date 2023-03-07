tag: user.single_application
-
^command mode$:
    mode.disable("user.single_application")
    mode.enable("command")
^dictation mode$:
    mode.disable("user.single_application")
    mode.enable("dictation")
