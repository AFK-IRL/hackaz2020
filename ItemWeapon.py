import random

class ItemWeapon:

    # melee is boolean
    def __init__(self, name, damage, ammo_type, miss_chance, melee):
        self._type = 'ItemWeapon'
        self._damage = damage
        self._ammo_type = ammo_type
        self._miss_chance = miss_chance
        self._melee = melee
        self._name = name

    def use_weapon(self):
        if not self._melee:
            return 0
            
        chance = random.randint(1,100)
        if chance > self._miss_chance:
               return self._damage
        return 0

    def get_type(self):
        return self._type

    def get_ammo_type(self):
        return self._ammo_type

    def get_name(self):
        return self._name
