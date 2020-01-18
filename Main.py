from Control import Control
import curses

control = Control(None)

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
begin_y = 0
begin_x = 0
#curses.resizeterm(char_height, char_width)
win.refresh()

gameOver = False

while not gameOver:
    ch = win.getkey()

    if ch == "q":
        gameOver = True

# Terminates curses application
curses.echo()
curses.nocbreak()
win.keypad(False)
curses.endwin()