import pygame
class Player:
    def __init__(self,x,y,speed,image_path):
        imagenOriginal = pygame.image.load(image_path).convert_alpha()
        scale = (64,64)
        self.image = pygame.transform.smoothscale(imagenOriginal,scale)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speed = speed 
        
    def update(self,keys,screen_width,screen_height):
        if keys [pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys [pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys [pygame.K_UP]:
            self.rect.y -= self.speed
        if keys [pygame.K_DOWN]:
            self.rect.y += self.speed

    def draw(self,surface):
        surface.blit(self.image,self.rect) 