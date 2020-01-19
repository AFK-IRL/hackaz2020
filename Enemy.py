import random

class Enemy:

    # difficulty is integer 0-2 (inclusive)
    def __init__(self, x, y, levelMap, difficulty=0, health=10, damage=2, miss_chance=20):
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
        roomBounds = self.levelMap.getRoomBounds(self.x, self.y)
        enemyLocationsInRoom = []
        for j in range(len(self.levelMap.enemies)):
            if (self.x, self.y) != (self.levelMap.enemies[j].x, self.levelMap.enemies[j].y):
                fellowEnemyRoomBounds = self.levelMap.getRoomBounds(self.levelMap.enemies[j].x, self.levelMap.enemies[j].y)
                if roomBounds == fellowEnemyRoomBounds:
                    enemyLocationsInRoom += (self.levelMap.enemies[j].x, self.levelMap.enemies[j].y)

        if random.random() < self.prob_to_move and self.alive:
            num = random.randint(1,4)
            if num == 1 and self.levelMap._map[self.y][self.x-1] == 0 and not (self.x - 1, self.y) in enemyLocationsInRoom:
                self.move_left()
            elif num == 2 and self.levelMap._map[self.y][self.x+1] == 0 and not (self.x + 1, self.y) in enemyLocationsInRoom:
                self.move_right()
            elif num == 3 and self.levelMap._map[self.y-1][self.x] == 0 and not (self.x, self.y - 1) in enemyLocationsInRoom:
                self.move_up()
            elif self.levelMap._map[self.y+1][self.x] == 0 and not (self.x, self.y + 1) in enemyLocationsInRoom:
                self.move_down()

    def move_left(self):
        if self.alive:
            self.x -= 1

    def move_right(self):
        if self.alive:
            self.x += 1

    def move_up(self):
        if self.alive:
            self.y -= 1

    def move_down(self):
        if self.alive:
            self.y += 1

    def take_damage(self, amt):
        self.health -= amt
        if self.health < 1:
            self.alive = False

    def is_dead(self):
        return self.health < 1

    def attack(self):
        chance = random.randint(1, 100)
        if chance > self.miss_chance:
            return self.damage
        return 0
