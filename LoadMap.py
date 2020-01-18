
class Map:

    def __init__(self, fileName):
        self._fileName = fileName
        self._map = []
        self.player = None
        self.enemies = None

        lines = []
        with open(fileName, 'r') as f:
            lines = f.readLines()
        for line in lines:
            line = line.replace('\n', '')
            line = line.replace('\r', '')
            arr = line.split()
            for i in range(len(arr)):
                if arr[i] == ' ':
                    arr[i] = 0
                else:
                    arr[i] = 1
            self._map += [arr]


    def update(self):
        return None

