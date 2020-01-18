import random

class ItemWeapon:

    # melee is boolean
    def __init__(self, damage, ammo_type, miss_chance, melee):
        self._type = 'ItemWeapon'
        self._damage = damage
        self._ammo_type = ammo_type
        self._ammo_count = 0
        self._miss_chance = miss_chance
        self._melee = melee

    def use_weapon(self):
        if not self._melee and self._ammo_count < 1:
            return 0

        if not self._melee:
            self._ammo_count -= 1
            
        chance = random.randint(1,100)
        if chance > self._miss_chance:
               return self._damage
        return 0

    def get_ammo_type(self):
        return self._ammo_type