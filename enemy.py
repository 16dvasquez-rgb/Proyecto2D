from player import Player
from time import sleep
class Enemy(Player):
    def __init__(self,x,y,speed,image_path="assets\enemy.jpg"):
        super().__init__(x,y,speed,image_path)

    def update(self, keys, screen_width, screen_height):
        if self.rect.x > screen_width-100 or self.rect.x < 100:
            self.speed *= -1

        self.rect.x += self.speed