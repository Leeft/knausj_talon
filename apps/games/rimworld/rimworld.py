from talon import Context, Module, actions

mod = Module()
ctx = Context()

apps = mod.apps
apps.rimworld ="""
os: windows
and app.exe: RimWorldWin64.exe
"""

ctx.matches = r"""
app: rimworld
"""

ctx.tags = ["user.single_application"]
