import random

class ItemWeapon:

    # melee is boolean
    def __init__(self, damage, ammo_type, miss_chance):
        self._type = 'ItemWeapon'
        self._damage = damage
        self._ammo_type = ammo_type
        self._miss_chance = 0

    def use_weapon(self):
        chance = random.randint(1,100)
        if chance > self._miss_chance:
               return self._damage
        return 0

    def get_ammo_type(self):
        return self._ammo_type