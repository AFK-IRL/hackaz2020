from Inventory import Inventory
from ItemWeapon import ItemWeapon

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ammo = 7
        self.healthPacks = 3
        self.inventory = Inventory()
        self._current_weapon = None
        self._health = 20
        self._maxHealth = self._health

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1

    def take_damage(self, amount):
        self._health -= amount

    def heal(self, amount):
        self._health += amount

    def is_dead(self):
        return self._health <= 0

    def equip_weapon(self, weapon_name):
        self._current_weapon = self.inventory.get_item(weapon_name)

    def use_weapon(self):
        if self._current_weapon != None:
            return self._current_weapon.use_weapon()

        return 0

