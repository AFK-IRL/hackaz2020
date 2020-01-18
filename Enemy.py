import random

class Enemy:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_bound = 0
        self.y_bound = 0
        self.prob_to_move = .5

    def move_random(self):
        if random.random() < prob_to_move:
            num = random.randint(1,4)
            if num == 1:
                self.move_left()
            elif num == 2:
                self.move_right()
            elif num == 3:
                self.move_up()
            else:
                self.move_down()

        }
        
        return switcher.get(random.randInt(0,4))

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y -= 1
    
    def move_down(self):
        self.y += 1