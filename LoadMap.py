from Player import Player
from Enemy import Enemy

class Map:
    path_char = '='
    wall_char = ' '

    def __init__(self, fileName):
        self._fileName = fileName
        self._map = []
        self.player = None
        self.enemies = []

        lines = []
        with open(fileName, 'r') as f:
            lines = f.readlines()
        row = 0
        for line in lines:
            line = line.replace('\n', '')
            line = line.replace('\r', '')
            arr = [char for char in line]
            for i in range(len(arr)):
                if arr[i] == '.':
                    arr[i] = 1
                else:
                    if arr[i] == '@':
                        self.player = Player(i, row)
                    if arr[i] == 'x':
                        self.enemies += [Enemy(i, row)]
                    arr[i] = 0
            self._map += [arr]
            row += 1


    def update(self):
        return None

    def getStrings(self):
        arr = []
        for i in range(30):
            arr += [""]
            for j in range(90):
                if self._map[i][j] == 0:
                    arr[i] += Map.path_char
                else:
                    arr[i] += Map.wall_char
        x = self.player.x
        y = self.player.y
        arr[y] = arr[y][:x] + '@' + arr[y][x+1:]
        for enemy in self.enemies:
            if not enemy.alive:
                continue
            x = enemy.x
            y = enemy.y
            arr[y] = arr[y][:x] + 'x' + arr[y][x+1:]
        return tuple(arr)

