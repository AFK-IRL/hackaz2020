import random
import curses

class Combat:

    def __init__(self, win, statWin, player, enemy):
        self._win = win
        self._statWin = statWin
        self._player = player
        self._enemy = enemy
        self._word_dic = { 0: ['fire', 'shoot', 'stab', 'bash', 'jab', 'smash'], 1: ['frustrating', 'complicated', 'ruminated'], 2: ['equanimity', 'blandishment', 'circumlocution']}
        self._cur_word = ''
        self._cur_word_list = []

    def setup(self):
        choice = random.randint(0,5)

        self._cur_word = self._word_dic[self._enemy.difficulty][choice]
        self._cur_word_list = list(self._cur_word)

    # returns 0 if enemy died, returns 1 if player died, returns 2 if quit game
    def fight(self):
        self._win.erase()
        self._win.border('|', '|', '-', '-', '+', '+', '+', '+')
        lines = []
        with open("robot.txt", 'r') as f:
            lines = f.readlines()
        row = 1
        for line in lines:
            line = line.replace('\n', '')
            line = line.replace('\r', '')
            self._win.addstr(row, 50, line)
            row += 1
        lines = []
        with open("cannon.txt", 'r') as f:
            lines = f.readlines()
        row = 17
        for line in lines:
            line = line.replace('\n', '')
            line = line.replace('\r', '')
            self._win.addstr(row, 7, line)
            row += 1
        enemyHealth = self._win.subwin(5, 46, 27, 46)
        textToType = self._win.subwin(5, 47, 27, 0)
        enemyHealth.refresh()

        while True:
            enemyHealth.erase()
            enemyHealth.border('|', '|', '-', '-', '+', '+', '+', '+')
            textToType.erase()
            textToType.border('|', '|', '-', '-', '+', '+', '+', '+')
            self._win.border('|', '|', '-', '-', '+', '+', '+', '+')
            self.setup()
            spelling = True
            currentSpelledWord = ""
            textToType.addstr(2, 2, "Spell '" + self.get_cur_word() + "'" + " | " + currentSpelledWord) 
            enemyHealth.addstr(2, 2, "Angry Robot HP: [" + ('#' * self._enemy.health) + (' ' * (self._enemy.maxHealth-self._enemy.health)) + "]")
            enemyHealth.refresh()
            textToType.refresh()
            while len(self._cur_word_list) > 0 and spelling:
                ch = self._win.getkey()

                self._win.erase()
                self._win.border('|', '|', '-', '-', '+', '+', '+', '+')
                lines = []
                with open("robot.txt", 'r') as f:
                    lines = f.readlines()
                row = 1
                for line in lines:
                    line = line.replace('\n', '')
                    line = line.replace('\r', '')
                    self._win.addstr(row, 50, line)
                    row += 1
                lines = []
                with open("cannon.txt", 'r') as f:
                    lines = f.readlines()
                row = 17
                for line in lines:
                    line = line.replace('\n', '')
                    line = line.replace('\r', '')
                    self._win.addstr(row, 7, line)
                    row += 1
                enemyHealth.erase()
                enemyHealth.border('|', '|', '-', '-', '+', '+', '+', '+')
                textToType.erase()
                textToType.border('|', '|', '-', '-', '+', '+', '+', '+')

                if ch == '`':
                    return 2
                elif ch == '.' and self._player.healthPacks > 0:
                    self._player.heal(self._player._maxHealth//2)
                    self._player.healthPacks -= 1
                    #self._statWin.erase()
                    self._statWin.addstr(2, 2, f"HP: " + str(self._player._health).ljust(2) + "[" + '#' * self._player._health + ' ' * (self._player._maxHealth-self._player._health) + ']')
                    self._statWin.addstr(3, 2, "Health Packs: " + str(self._player.healthPacks) + " (Press . to heal)")
                    self._statWin.refresh()
                elif ch != self._cur_word_list[0]:
                    spelling = False
                else:
                    currentSpelledWord += ch
                    self._cur_word_list.pop(0)

                textToType.addstr(2, 2, "Spell '" + self.get_cur_word() + "'" + " | " + currentSpelledWord) 
                enemyHealth.addstr(2, 2, "Angry Robot HP: [" + '#' * self._enemy.health + ' ' * (self._enemy.maxHealth-self._enemy.health) + "]")
                enemyHealth.refresh()
                textToType.refresh()

            damage = 0
            self._player.ammo -= 1
            if spelling:
                damage = self._player.use_weapon()
                self._win.erase()
                self._win.border('|', '|', '-', '-', '+', '+', '+', '+')
                lines = []
                with open("robot2.txt", 'r') as f:
                    lines = f.readlines()
                row = 2
                for line in lines:
                    line = line.replace('\n', '')
                    line = line.replace('\r', '')
                    self._win.addstr(row, 50, line)
                    row += 1
                lines = []
                with open("cannon2.txt", 'r') as f:
                    lines = f.readlines()
                row = 17
                for line in lines:
                    line = line.replace('\n', '')
                    line = line.replace('\r', '')
                    self._win.addstr(row, 6, line)
                    row += 1
                self._win.refresh()
                self._enemy.take_damage(damage)

            if self._enemy.is_dead():
                self._player.ammo += 6
                return 0

            self._player.take_damage(self._enemy.attack())
            self._statWin.addstr(2, 2, f"HP: " + str(self._player._health).ljust(2) + "[" + '#' * self._player._health + ' ' * (self._player._maxHealth-self._player._health) + ']')
            self._statWin.addstr(3, 2, "Health Packs: " + str(self._player.healthPacks) + " (Press . to heal)")

            self._statWin.refresh()
            if self._player.is_dead():
                return 1

    def get_cur_word(self):
        return self._cur_word
