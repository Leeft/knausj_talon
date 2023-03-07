# -1 because we are repeating, so the initial command counts as one
<user.ordinals>: core.repeat_command(ordinals - 1)
<number_small> times: core.repeat_command(number_small - 1)
(repeat that | twice): core.repeat_command(1)
parrot(palate_click):
    user.hud_add_log('event', 'repeating phrase (palate_click)')
    core.repeat_phrase(1)
parrot(cluck):
    user.hud_add_log('event', 'repeating phrase (cluck)')
    core.repeat_phrase(1)
repeat that <number_small> [times]: core.repeat_command(number_small)
