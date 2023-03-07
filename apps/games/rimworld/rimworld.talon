app.exe: RimWorldWin64.exe
mode: user.single_application
-
normal: key(1)
fast: key(2)
fastest: key(3)
slower: key(end)
faster: key(home)
pause: key("space")
( last | previous ) [ colonist ]: key(,)
next [ colonist ]: key(,)
( rot | rotate ) left: key(q)
( rot | rotate ) right: key(e)
flip blueprint: key(f)
accept: key(enter)
cancel: key(escape)
heat [map]: key(\)
[toggle] room stats: key(g)
[toggle] beauty (display): key(t)
[toggle] power: key(v)
[toggle] forbidden: key(f)
draft: key(r)
[go] up: key(up)
[go] down: key(down)
[go] left: key(left)
[go] right: key(right)
zoom in: key(pagedown)
zoom out: key(pageup)
toggle architect [tab]: key(tab)
toggle work [tab]: key(f1)
toggle schedule [tab]: key(f2)
toggle assign [tab]: key(f3)
toggle animals [tab]: key(f4)
toggle wildlife [tab]: key(f5)
toggle research [tab]: key(f6)
toggle quests [tab]: key(f7)
toggle world [tab]: key(f8)
toggle history [tab]: key(f9)

# noise(cluck): mouse.click()

# touch:
#     mouse_click(0)
#     # close the mouse grid if open
#     user.grid_close()
#     # End any open drags
#     # Touch automatically ends left drags so this is for right drags specifically
#     user.mouse_drag_end()
