from Player import Player
from Enemy import Enemy
from LoadMap import Map

class Control:

    def __init__(self, map_file):
        self.levelMap = Map(map_file)
        self.player = self.levelMap.player
        self.enemies = self.levelMap.enemies
