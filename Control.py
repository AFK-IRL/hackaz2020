from Player import Player
from Enemy import Enemy
from LoadMap import Map
from ItemWeapon import ItemWeapon

class Control:

    def __init__(self, map_file):
        self.levelMap = Map(map_file)
        self.player = self.levelMap.player
        self.enemies = self.levelMap.enemies
        self.player._current_weapon = ItemWeapon('knife', 3, None, 1, True)
