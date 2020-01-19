from Control import Control
from LoadMap import Map
from Combat import Combat
import curses, curses.panel
from Inventory import Inventory
from ItemWeapon import ItemWeapon

win = curses.initscr()
mapWin = win.subwin(32, 92, 0, 0)
mapWin.border('|', '|', '-', '-', '+', '+', '+', '+')
statWin = win.subwin(6, 77, 31, 0)
statWin.border('|', '|', '-', '-', '+', '+', '+', '+')
helpWin = win.subwin(6, 16, 31, 76)
helpWin.border('|', '|', '-', '-', '+', '+', '+', '+')

control = Control("map.txt")
control.player.inventory.add_item(ItemWeapon('plasma', 5, "Plasma Bolts", 0, 0))

default_cursor_visibility = curses.curs_set(0)

# Turn off key echoing
curses.noecho()

# Initialize key listening
curses.cbreak()

# Enable listening from the keypad (Arrow keys, Home, Insert, etc.)
win.keypad(True)

# Init Help Panel
helpWin.addstr(1, 2, "WASD/arrows:")
helpWin.addstr(2, 2, "for movement")
helpWin.addstr(4, 2, "` to quit")
helpWin.refresh()

# Init Stats Panel
#statWin.addstr(1, 2, f"Health Points: {control.player._health}")
#statWin.addstr(2, 2, f"Total Ammo: {control.player.ammo}")
#statWin.refresh()

def updateStats():
    statWin.erase()
    statWin.border('|', '|', '-', '-', '+', '+', '+', '+')
    statWin.addstr(1, 2, "HP: " + str(control.player._health).ljust(2) + "[" + ('#' * control.player._health) + (' ' * (control.player._maxHealth-control.player._health)) + ']')
    statWin.addstr(2, 2, f"Total Ammo: {control.player.ammo}")
    statWin.addstr(3, 2, "Health Packs: " + str(control.player.healthPacks) + " (Press . to heal)")
    statWin.refresh()

updateStats()

# Init window
def resetConsole():
    curses.echo()
    curses.nocbreak()
    win.keypad(False)
    curses.curs_set(default_cursor_visibility)
    curses.endwin()
    bottomPanel = curses.panel.new_panel(win)

char_height = 37
char_width = 92

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
won = -1

def updateInMap():
    global gameOver, inCombat, currentEnemy
    row = 1
    for line in control.levelMap.getRevealedStrings():
        mapWin.addstr(row, 1, line)
        row += 1

    #win.addstr(30, 0, f"({control.player.x}, {control.player.y})             ")
    #win.addstr(31, 0, str([(enemy.x,enemy.y) for enemy in control.enemies]))

    mapWin.refresh()
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
    if ch == "." and control.player.healthPacks > 0:
        control.player.heal(control.player._maxHealth//2)
        control.player.healthPacks -= 1
        updateStats()
    if ch == "`":
        gameOver = True
        return

    control.levelMap.revealRoom(control.player.x, control.player.y)
    control.levelMap.revealPath(control.player.x, control.player.y)

    # check if player is on enemy
    #for i in range(len(control.enemies)):
    #    if control.player.x == control.enemies[i].x and control.player.y == control.enemies[i].y and control.enemies[i].alive:
    #        inCombat = True
    #        currentEnemy = i
            #win.addstr(32, 0, "combat!!")
    #        return updateInCombat()

    # move enemies
    for i in range(len(control.enemies)):
        enemyLocationsInRoom = []
        roomBounds = control.levelMap.getRoomBounds(control.player.x, control.player.y)
        for j in range(len(control.enemies)):
                if i != j:
                    fellowEnemyRoomBounds = control.levelMap.getRoomBounds(control.enemies[j].x, control.enemies[j].y)
                    if roomBounds == fellowEnemyRoomBounds:
                        enemyLocationsInRoom += (control.enemies[j].x, control.enemies[j].y)

        if control.levelMap._map[control.player.y][control.player.x] == 0 and control.enemies[i].x >= roomBounds[0] and control.enemies[i].x <= roomBounds[1] and control.enemies[i].y >= roomBounds[2] and control.enemies[i].y <= roomBounds[3]:
            enemyLocationsInRoom = []

            if control.enemies[i].x > control.player.x and not (control.enemies[i].x - 1, control.enemies[i].y) in enemyLocationsInRoom:
                control.enemies[i].move_left()
            if control.enemies[i].x < control.player.x and not (control.enemies[i].x + 1, control.enemies[i].y) in enemyLocationsInRoom:
                control.enemies[i].move_right()
            if control.enemies[i].y > control.player.y and not (control.enemies[i].x, control.enemies[i].y - 1) in enemyLocationsInRoom:
                control.enemies[i].move_up()
            if control.enemies[i].y < control.player.y and not (control.enemies[i].x, control.enemies[i].y + 1) in enemyLocationsInRoom:
                control.enemies[i].move_down()
        else:
            control.enemies[i].move_random()

    # check if enemy moved onto player
    for i in range(len(control.enemies)):
        if control.player.x == control.enemies[i].x and control.player.y == control.enemies[i].y and control.enemies[i].alive:
            inCombat = True
            currentEnemy = i
            return updateInCombat()

def updateInCombat():
    global gameOver, inCombat, currentEnemy, won
    #for i in range(1, 31):
    #    win.addstr(i, 1, ' '*90)

    combat = Combat(mapWin, statWin, control.player, control.enemies[currentEnemy])

    #win.addstr(1, 2, "combat goes here...")
    #win.addstr(2, 2, "press any key to continue (` still quits)")

    #mapWin.refresh()
    #ch = win.getkey()

    fightOutcome = combat.fight()

    mapWin.border('|', '|', '-', '-', '+', '+', '+', '+')

    if fightOutcome == 2 or fightOutcome == 1:
        gameOver = True
        inCombat = False
        won = 0
        return
    elif fightOutcome == 0:
        control.enemies[currentEnemy].alive = False
        inCombat = False
        currentEnemy = None
        return

while not gameOver:
    if sum([1 if enemy.alive else 0 for enemy in control.enemies]) == 0:
        won = 1
        break
    #win.addstr(33, 0, f'{gameOver}')
    if inCombat:
        updateInCombat()
    else:
        updateInMap()
    win.refresh()

# Terminates curses application
resetConsole()
if won == 1:
    print("Congrats! You win!")
elif won == 0:
    print("You lose... Better luck next time.")
