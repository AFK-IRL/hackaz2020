import random
import curses

class Combat:

    def __init__(self, win, statWin, player, enemy):
        self._win = win
        self._statWin = statWin
        self._player = player
        self._enemy = enemy
        self._word_dic = { 0: ['hello', 'could', 'weight'], 1: ['frustrating', 'complicated', 'ruminated'], 2: ['equanimity', 'blandishment', 'circumlocution']}
        self._cur_word = ''
        self._cur_word_list = []

    def setup(self):
        choice = random.randint(0,2)

        self._cur_word = self._word_dic[self._enemy.difficulty][choice]
        self._cur_word_list = list(self._cur_word)

    # returns 0 if enemy died, returns 1 if player died, returns 2 if quit game
    def fight(self):
        self._win.erase()
        enemyHealth = self._win.subwin(5, 46, 27, 46)
        textToType = self._win.subwin(5, 47, 27, 0)

        while True:
            enemyHealth.erase()
            enemyHealth.border('|', '|', '-', '-', '+', '+', '+', '+')
            textToType.erase()
            textToType.border('|', '|', '-', '-', '+', '+', '+', '+')
            self._win.border('|', '|', '-', '-', '+', '+', '+', '+')
            self.setup()
            spelling = True
            currentSpelledWord = ""
            textToType.addstr(2, 2, self.get_cur_word() + " | " + currentSpelledWord) 
            enemyHealth.addstr(2, 2, "[" + ('#' * self._enemy.health) + (' ' * (self._enemy.maxHealth-self._enemy.health)) + "]")
            enemyHealth.refresh()
            textToType.refresh()
            while len(self._cur_word_list) > 0 and spelling:
                ch = self._win.getkey()

                if ch == '`':
                    return 2
                if ch != self._cur_word_list[0]:
                    spelling = False

                currentSpelledWord += ch
                textToType.addstr(2, 2, self.get_cur_word() + " | " + currentSpelledWord) 
                enemyHealth.addstr("[" + '#' * self._enemy.health + ' ' * (self._enemy.maxHealth-self._enemy.health) + "]")
                enemyHealth.refresh()
                textToType.refresh()
                self._cur_word_list.pop(0)

            damage = 0
            if spelling:
                damage = self._player.use_weapon()

            self._enemy.take_damage(damage)

            if self._enemy.is_dead():
                return 0

            self._player.take_damage(self._enemy.attack())
            self._statWin.addstr(1, 2, f"HP: {self._player._health} [" + '#' * self._player._health + ' ' * (self._player._maxHealth-self._player._health) + ']')
            self._statWin.addstr(2, 2, f"Total Ammo: {self._player.ammo}")

            self._statWin.refresh()
            if self._player.is_dead():
                return 1

    def get_cur_word(self):
        return self._cur_word
        

    

    
