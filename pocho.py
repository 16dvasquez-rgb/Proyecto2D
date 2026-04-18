import pygame
class Pocho(pygame.sprite.sprite):
    def __init__(self,x,y,speed,image_path=""):
        super().__init__()
        imagenOriginal = pygame.image.load(image_path).convert_alpha()
        scale = (50,50)
        self.image = pygame.transform.smoothscale(imagenOriginal,scale)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speed = speed
        self.boost_end_time = 0
        self.normal_speed = speed

    def update(self,keys,screen_width,screen_height,walls_group):

        move_x = 0

        if keys [pygame.K_LEFT]:
            move_x = -self.speed
        if keys [pygame.K_RIGHT]:
            move_x = self.speed

        self.rect.x += move_x

        self.checkWallColisionX(walls_group,move_x)

        move_y = 0

        if keys [pygame.K_UP]:
            move_y = -self.speed
        if keys [pygame.K_DOWN]:
            move_y = self.speed

        self.rect.y += move_y

        self.checkWallColisionY(walls_group,move_y)

    def draw(self,surface):
        surface.blit(self.image,self.rect) 
    
    def setupPosition(self,x,y):
        self.rect.center = (x,y)

    def checkWallColisionX(self,walls_group,move_x):
        hits = pygame.sprite.spritecollide(self,walls_group,False)
        for walls in hits:
            if move_x > 0:
                self.rect.right = walls.rect.left
            elif move_x < 0:
                self.rect.left = walls.rect.right

    def checkWallColisionY(self,walls_group,move_y):
        hits = pygame.sprite.spritecollide(self,walls_group,False)
        for walls in hits:
            if move_y > 0:
                self.rect.bottom = walls.rect.top
            elif move_y < 0:
                self.rect.top = walls.rect.bottom

    def checkenemycolision (self,enemy_group):
        hits = pygame.sprite.spritecollide(self,enemy_group,False)

        if hits:
            return True
        else:
            return False
