import pygame
from player import Player
# from enemy import Enemy
# from wall import Wall
from map import Map

#para que la libreria pygame funcione y todo funcione tambien
pygame.init ()

class App():
    def __init__(self,backgroundColor,caption,width=0,height=0):    

        pygame.init() 

        # Si el usuario pone 0, 0 asumimos pantalla completa 
        if width == 0 or height == 0: 
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) 
        else: 
            self.screen = pygame.display.set_mode((width, height))

        # Actualizamos ancho y alto reales 
        self.width, self.height = self.screen.get_size()

        self.backgroundColor = backgroundColor
        self.running = True
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.caption = pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.player = Player(0,0,15)
        self.enemies = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.map = Map()
        self.map.setup(self.walls,self.enemies,self.player)

    def run(self):
        while self.running:

            #obtenemos y revisamos todos los eventos que se han ejecutado en el juego
            for event in pygame.event.get():

                #aqui validamos si ejecuto el evento de cerrar la ventana (le dimos click a la x)
                if event.type == pygame.QUIT:
                    #si se ejecuto el evento de cerrar ventana hacemos que running se igual a false 
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            
            keys = pygame.key.get_pressed()
            self.player.update(keys,self.width,self.height,self.walls)
            self.enemies.update(keys,self.width,self.height)
            self.screen.fill(self.backgroundColor)
            self.player.draw(self.screen)
            self.enemies.draw(self.screen)
            self.walls.draw(self.screen)

            if self.player.checkenemycolision(self.enemies):
                self.running = False

            #actulizamos la ventana
            pygame.display.flip()

            #los frames por segundo     
            self.clock.tick (1000)

        

        