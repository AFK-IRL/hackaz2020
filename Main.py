from Control import Control
from LoadMap import Map
import curses

win = curses.initscr()

control = Control("map.txt")

map = Map("map.txt")

default_cursor_visibility = curses.curs_set(0)

# Turn off key echoing
curses.noecho()

# Initialize key listening
curses.cbreak()

# Enable listening from the keypad (Arrow keys, Home, Insert, etc.)
win.keypad(True)

# Init window
char_height = 35
char_width = 90

actual_height, actual_width = win.getmaxyx()

if char_height > actual_height or char_width > actual_width:
    curses.echo()
    curses.nocbreak()
    win.keypad(False)
    curses.curs_set(default_cursor_visibility)
    curses.endwin()
    print(f"Window size must be at least {char_width}x{char_height}")
    print(f"Window size is currently {actual_width}x{actual_height}")
    print("Please resize window and relaunch")
    exit(1)

begin_y = 0
begin_x = 0
#curses.resizeterm(char_height, char_width)
win.refresh()

gameOver = False

while not gameOver:
    #win.addstr(map._map)
    row = 0
    for line in control.levelMap.getRevealedStrings():
        win.addstr(row, 0, line)
        row += 1

    ch = win.getkey()

    if ch == "w" and control.player.y > 0 and (control.levelMap._map[control.player.y-1][control.player.x] == 0 or control.levelMap._map[control.player.y-1][control.player.x] == 2):
        control.player.move_up()
    if ch == "a" and control.player.x > 0 and (control.levelMap._map[control.player.y][control.player.x-1] == 0 or control.levelMap._map[control.player.y][control.player.x-1] == 2):
        control.player.move_left()
    if ch == "s" and control.player.y < actual_height - 1 and (control.levelMap._map[control.player.y+1][control.player.x] == 0 or control.levelMap._map[control.player.y+1][control.player.x] == 2):
        control.player.move_down()
    if ch == "d" and control.player.x < actual_width - 1 and (control.levelMap._map[control.player.y][control.player.x+1] == 0 or control.levelMap._map[control.player.y][control.player.x+1] == 2):
        control.player.move_right()
    if ch == "q":
        gameOver = True

    control.levelMap.revealRoom(control.player.x, control.player.y)
    control.levelMap.revealPath(control.player.x, control.player.y)

    win.addstr(str(control.levelMap._revealedMap[control.player.y][control.player.y]))

    win.refresh()

# Terminates curses application
curses.echo()
curses.nocbreak()
win.keypad(False)
curses.curs_set(default_cursor_visibility)
curses.endwin()
