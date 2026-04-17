import pygame
import random

from player import Player

class Enemy(Player):
    def __init__(self, x, y, speed, image_path="assets/Enemy.png"):
        super().__init__(x, y, speed, image_path)
        # Elegir una dirección aleatoria inicial (arriba, abajo, izquierda, derecha)
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.direction = random.choice(self.directions)
        # Temporizador para cambiar de dirección aleatoriamente
        self.change_timer = 0
        self.change_interval = random.randint(60, 180)  # cambiar cada 1-3 segundos (a 60fps)

    def update(self, keys, screen_width, screen_height, walls_group):
        self.change_timer += 1

        # Cada cierto tiempo, hay probabilidad de cambiar dirección al azar
        if self.change_timer >= self.change_interval:
            self.change_timer = 0
            self.change_interval = random.randint(60, 180)
            self.direction = random.choice(self.directions)

        # Calcular movimiento en X
        move_x = self.direction[0] * self.speed
        self.rect.x += move_x
        # Revisar colisión con paredes en X
        hit_wall_x = self.checkWallColisionXEnemy(walls_group, move_x)

        # Calcular movimiento en Y
        move_y = self.direction[1] * self.speed
        self.rect.y += move_y
        # Revisar colisión con paredes en Y
        hit_wall_y = self.checkWallColisionYEnemy(walls_group, move_y)

        # Si chocó con una pared, elegir una nueva dirección al azar
        if hit_wall_x or hit_wall_y:
            # Filtrar la dirección actual para no volver a elegirla
            otras_direcciones = [d for d in self.directions if d != self.direction]
            self.direction = random.choice(otras_direcciones)
            self.change_timer = 0

    def checkWallColisionXEnemy(self, walls_group, move_x):
        """Revisa colisión en X y retorna True si hubo colisión"""
        hits = pygame.sprite.spritecollide(self, walls_group, False)
        if hits:
            for wall in hits:
                if move_x > 0:
                    self.rect.right = wall.rect.left
                elif move_x < 0:
                    self.rect.left = wall.rect.right
            return True
        return False

    def checkWallColisionYEnemy(self, walls_group, move_y):
        """Revisa colisión en Y y retorna True si hubo colisión"""
        hits = pygame.sprite.spritecollide(self, walls_group, False)
        if hits:
            for wall in hits:
                if move_y > 0:
                    self.rect.bottom = wall.rect.top
                elif move_y < 0:
                    self.rect.top = wall.rect.bottom
            return True
        return False