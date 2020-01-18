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
def resetConsole():
    curses.echo()
    curses.nocbreak()
    win.keypad(False)
    curses.curs_set(default_cursor_visibility)
    curses.endwin()

char_height = 35
char_width = 90

actual_height, actual_width = win.getmaxyx()

if char_height > actual_height or char_width > actual_width:
    resetConsole()
    print(f"Window size must be at least {char_width}x{char_height}")
    print(f"Window size is currently {actual_width}x{actual_height}")
    print("Please resize window and relaunch")
    exit(1)

begin_y = 0
begin_x = 0
#curses.resizeterm(char_height, char_width)
win.refresh()

inCombat = False
currentEnemy = None
gameOver = False



def updateInMap():
    global gameOver, inCombat, currentEnemy
    row = 0
    for line in control.levelMap.getRevealedStrings():
        win.addstr(row, 0, line)
        row += 1

    #win.addstr(30, 0, f"({control.player.x}, {control.player.y})             ")
    #win.addstr(31, 0, str([(enemy.x,enemy.y) for enemy in control.enemies]))

    ch = win.getkey()

    if ch == "w" or ch == "KEY_UP":
        if control.player.y > 0 and (control.levelMap._map[control.player.y-1][control.player.x] == 0 or control.levelMap._map[control.player.y-1][control.player.x] == 2):
            control.player.move_up()
    if ch == "a" or ch == "KEY_LEFT":
        if control.player.x > 0 and (control.levelMap._map[control.player.y][control.player.x-1] == 0 or control.levelMap._map[control.player.y][control.player.x-1] == 2):
            control.player.move_left()
    if ch == "s" or ch == "KEY_DOWN":
        if control.player.y < actual_height - 1 and (control.levelMap._map[control.player.y+1][control.player.x] == 0 or control.levelMap._map[control.player.y+1][control.player.x] == 2):
            control.player.move_down()
    if ch == "d" or ch == "KEY_RIGHT":
        if control.player.x < actual_width - 1 and (control.levelMap._map[control.player.y][control.player.x+1] == 0 or control.levelMap._map[control.player.y][control.player.x+1] == 2):
            control.player.move_right()
    if ch == "q":
        gameOver = True
        return

    control.levelMap.revealRoom(control.player.x, control.player.y)
    control.levelMap.revealPath(control.player.x, control.player.y)

    # check if player is on enemy
    for i in range(len(control.enemies)):
        if control.player.x == control.enemies[i].x and control.player.y == control.enemies[i].y:
            inCombat = True
            currentEnemy = i
            #win.addstr(32, 0, "combat!!")
            return updateInCombat()

    # TODO move enemies

    # check if enemy moved onto player
    for i in range(len(control.enemies)):
        if control.player.x == control.enemies[i].x and control.player.y == control.enemies[i].y:
            inCombat = True
            currentEnemy = i
            return updateInCombat()

def updateInCombat():
    global gameOver, inCombat, currentEnemy
    for i in range(30):
        win.addstr(i, 0, ' '*90)
    win.addstr(1, 1, "combat goes here...")
    win.addstr(2, 1, "press any key to continue (q still quits)")
    win.addstr(32, 0, "        ")
    ch = win.getkey()
    if ch == "q":
        gameOver = True
        return
    inCombat = False
    currentEnemy = None

while not gameOver:
    #win.addstr(33, 0, f'{gameOver}')
    if inCombat:
        updateInCombat()
    else:
        updateInMap()
    win.refresh()

# Terminates curses application
resetConsole()
