from Control import Control
from LoadMap import Map
import curses

control = Control(None)

map = Map("map.txt")

win = curses.initscr()

# Turn off key echoing
curses.noecho()

# Initialize key listening
curses.cbreak()

# Enable listening from the keypad (Arrow keys, Home, Insert, etc.)
win.keypad(True)

# Init window
char_height = 40
char_width = 160

actual_height, actual_width = win.getmaxyx()

if char_height != actual_height or char_width != actual_width:
    curses.echo()
    curses.nocbreak()
    win.keypad(False)
    curses.endwin()
    print(f"Window size must be {char_width}x{char_height}")
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

    ch = win.getkey()

    if ch == "q":
        gameOver = True

# Terminates curses application
curses.echo()
curses.nocbreak()
win.keypad(False)
curses.endwin()
