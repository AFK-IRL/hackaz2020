from Inventory import Inventory

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.inventory = Inventory()

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1
