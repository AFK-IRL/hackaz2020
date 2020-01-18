from Player import Player
from Enemy import Enemy

class Map:
    room_char = '='
    wall_char = ' '
    path_char = '#'

    def __init__(self, fileName, win):
        self.win = win
        self._fileName = fileName
        self._map = []
        self._revealedMap = []
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
            revArr = [char for char in line]
            for i in range(len(arr)):
                revArr[i] = 1
                if arr[i] == '.':
                    arr[i] = 1
                elif arr[i] == '=':
                    arr[i] = 2
                else:
                    if arr[i] == '@':
                        self.player = Player(i, row)
                    if arr[i] == 'x':
                        self.enemies += [Enemy(i, row)]
                    arr[i] = 0
            self._map += [arr]
            self._revealedMap += [revArr]
            row += 1

        self.revealRoom(self.player.x, self.player.y)
        self.revealPath(self.player.x, self.player.y)

    def update(self):
        return None

    def getRoomBounds(self, x, y):
        leftBound = x
        rightBound = x
        upperBound = y
        lowerBound = y

        foundLeftBound = False
        foundRightBound = False
        foundUpperBound = False
        foundLowerBound = False

        if self._map[y][x] == 0:
            while True:
                if leftBound > 0 and self._map[y][leftBound - 1] == 0:
                    leftBound -= 1
                else:
                    foundLeftBound = True

                if rightBound < 89 and self._map[y][rightBound + 1] == 0:
                    rightBound += 1
                else:
                    foundRightBound = True

                if upperBound > 0 and self._map[upperBound - 1][x] == 0:
                    upperBound -= 1
                else:
                    foundUpperBound = True

                if lowerBound < 29 and self._map[lowerBound + 1][x] == 0:
                    lowerBound += 1
                else:
                    foundLowerBound = True

                if foundLeftBound and foundRightBound and foundUpperBound and foundLowerBound:
                    break

        return [leftBound, rightBound, upperBound, lowerBound]

    def getStrings(self):
        arr = []
        for i in range(30):
            arr += [""]
            for j in range(90):
                if self._map[i][j] == 0:
                    arr[i] += Map.room_char
                elif self._map[i][j] == 1:
                    arr[i] += Map.wall_char
                elif self._map[i][j] == 2:
                    arr[i] += Map.path_char
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

    def revealPath(self, x, y):
        roomBounds = self.getRoomBounds(x, y)

        roomBounds[0] -= 1
        roomBounds[0] = max(roomBounds[0], 0)
        roomBounds[1] += 1
        roomBounds[1] = min(roomBounds[1], 89)
        roomBounds[2] -= 1
        roomBounds[2] = max(roomBounds[2], 0)
        roomBounds[3] += 1
        roomBounds[3] = min(roomBounds[3], 29)

        for i in range(roomBounds[2], roomBounds[3]+1):
            for j in range(roomBounds[0], roomBounds[1]+1):
                if self._map[i][j] == 2:
                    self.revealPathRecurse(j, i)

    def revealPathRecurse(self, x, y, visited=set()):
        if self._revealedMap[y][x] != 1:
            return
        if (x, y) in visited:
            return
        visited.add((x, y))

        if self._map[y][x] == 2:
            self._revealedMap[y][x] = 2
            if x - 1 >= 0 and self._map[y][x-1] == 2 and self._revealedMap[y][x-1] == 1:
                self.revealPathRecurse(x-1, y)
            if x + 1 < 90 and self._map[y][x+1] == 2 and self._revealedMap[y][x+1] == 1:
                self.revealPathRecurse(x+1, y)
            if y - 1 >= 0 and self._map[y-1][x] == 2 and self._revealedMap[y-1][x] == 1:
                self.revealPathRecurse(x, y-1)
            if y + 1 < 30 and self._map[y+1][x] == 2 and self._revealedMap[y+1][x] == 1:
                self.revealPathRecurse(x, y+1)

    def revealRoom(self, x, y, visited=set()):
        if self._revealedMap[y][x] != 1:
            return
        if (x, y) in visited:
            return
        visited.add((x, y))
        roomBounds = self.getRoomBounds(x, y)
        for i in range(roomBounds[2], roomBounds[3]+1):
            for j in range(roomBounds[0], roomBounds[1]+1):
                if self._map[i][j] == 0:
                    self._revealedMap[i][j] = 0
                    if j - 1 >= 0 and self._map[i][j-1] == 0 and self._revealedMap[i][j-1] == 1:
                        self.revealRoom(j-1, i)
                    if j + 1 < 90 and self._map[i][j+1] == 0 and self._revealedMap[i][j+1] == 1:
                        self.revealRoom(j+1, i)
                    if i - 1 >= 0 and self._map[i-1][j] == 0 and self._revealedMap[i-1][j] == 1:
                        self.revealRoom(j, i-1)
                    if i + 1 < 30 and self._map[i+1][j] == 0 and self._revealedMap[i+1][j] == 1:
                        self.revealRoom(j, i+1)

    def getRevealedStrings(self):
        arr = []
        for i in range(30):
            arr += [""]
            for j in range(90):
                if self._revealedMap[i][j] == 0:
                    arr[i] += Map.room_char
                elif self._revealedMap[i][j] == 1:
                    arr[i] += Map.wall_char
                elif self._revealedMap[i][j] == 2:
                    arr[i] += Map.path_char
        x = self.player.x
        y = self.player.y
        arr[y] = arr[y][:x] + '@' + arr[y][x+1:]
        for enemy in self.enemies:
            if self._revealedMap[enemy.y][enemy.x] == 0 and not enemy.alive:
                continue
            x = enemy.x
            y = enemy.y
            arr[y] = arr[y][:x] + 'x' + arr[y][x+1:]
        return tuple(arr)
