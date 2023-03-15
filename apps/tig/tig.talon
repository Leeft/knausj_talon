tag: terminal
and tag: user.tig
-
tig {user.tig_command} [<user.tig_arguments>]:
    args = tig_arguments or ""
    "tig {tig_command}{args} "

# Optimistic execution for frequently used commands that are harmless (don't
# change repository or index state).
tig refs$: "tig refs\n"
tig stash$: "tig stash\n"
tig status$: "tig status\n"

# Convenience
# tig add highlighted:
#     edit.copy()
#     insert("tig add ")
#     edit.paste()
#     key(enter)
# tig add clipboard:
#     insert("tig add ")
#     edit.paste()
#     key(enter)
# tig commit highlighted:
#     edit.copy()
#     insert("tig add ")
#     edit.paste()
#     insert("\ntig commit\n")
