
class Map:

    def __init__(self, fileName):
        self._fileName = fileName
        self._map = [[]]
        self.player = None
        self.enemies = None

        with file(fileName, 'r') as f:
            pass

    def update(self):
        return None

