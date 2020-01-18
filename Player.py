from Inventory import Inventory

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.inventory = Inventory()

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1
        self._health = 100
        self._current_weapon = ''

    def take_damage(self, amount):
        self._health -= amount

    def heal(self, amount):
        self._health += amount

    def is_alive(self):
        return self._health > 0

    def equip_weapon(self, weapon_name):
        self._current_weapon = self.inventory.get_item(weapon_name)

    def use_weapon(self):
        if self._current_weapon != None:

