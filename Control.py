from Player import Player
from Enemy import Enemy
from LoadMap import Map

class Control:

    def __init__(self, map_file, win):
        self.levelMap = Map(map_file, win)
        self.player = self.levelMap.player
        self.enemies = self.levelMap.enemies
