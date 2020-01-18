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
win.resize(char_height, char_width)

gameOver = False

while not gameOver:
    ch = win.getch()
    
    if ch == ord('q'):
        gameOver = True

# Terminates curses application
curses.nocbreak()
win.keypad(False)
curses.echo()