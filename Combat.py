import random
import curses

class Combat:

    def __init__(self, win, player, enemy):
        self._win = win
        self._player = player
        self._enemy = enemy
        self._word_dic = { 0: ['hello', 'could', 'weight'], 1: ['frustrating', 'complicated', 'ruminated'], 2: ['equanimity', 'blandishment', 'circumlocution']}
        self._cur_word = ''
        self._cur_word_list = []

    
    def setup(self):
        choice = random.randint(0,2)

        self._cur_word = self._word_dic[self._enemy.difficulty][choice]
        self._cur_word_list = list(self._cur_word)

    # returns 0 if enemy died, returns 1 if player died
    def fight(self):
        
        while True:
            self.setup()
            spelling = True
            while len(self._cur_word_list) > 0 and spelling:
                ch = self._win.getkey()

                if ch != self._cur_word_list[0]:
                    spelling = False
                
                self._cur_word_list.pop(0)

            damage = 0
            if spelling:
                damage = self._player.use_weapon()

            self._enemy.take_damage(damage)

            if self._enemy.is_dead():
                return 0

            self._player.take_damage(self._enemy.attack())
            if self._player.is_dead():
                return 1

    def get_cur_word(self):
        return self._cur_word
        

    

    
