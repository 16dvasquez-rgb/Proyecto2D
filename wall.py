import pygame
class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,color=(0,0,0)):
        super().__init__()
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

    def draw(self,surface):
        surface.blit(self.image,self.rect) 