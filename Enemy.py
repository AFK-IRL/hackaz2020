import random

class Enemy:

    # difficulty is integer 0-2 (inclusive)
    def __init__(self, x, y, levelMap, difficulty=None, health=10, damage=2, miss_chance=20):
        self.x = x
        self.y = y
        self.x_bound = 0
        self.y_bound = 0
        self.levelMap = levelMap
        self.prob_to_move = 0.25
        self.alive = True
        self.difficulty = difficulty
        self.health = health
        self.damage = damage
        self.miss_chance = miss_chance

    def move_random(self):
        if random.random() < self.prob_to_move:
            num = random.randint(1,4)
            if num == 1 and self.levelMap[self.y][self.x-1] == 0:
                self.move_left()
            elif num == 2 and self.levelMap[self.y][self.x+1] == 0:
                self.move_right()
            elif num == 3 and self.levelMap[self.y-1][self.x] == 0:
                self.move_up()
            elif self.levelMap[self.y+1][self.x] == 0:
                self.move_down()

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y -= 1
    
    def move_down(self):
        self.y += 1

    def take_damage(self, amt):
        self.health -= amt

    def is_dead(self):
        return self.health < 1

    def attack(self):
        chance = random.randint(1, 100)
        if chance > self.miss_chance:
            return self.damage
        return 0
