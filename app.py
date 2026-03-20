import pygame
from player import Player
from map import Map
from camera import Camera

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
        self.player = Player(0,0,10)
        self.enemies = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.map = Map()
        self.map.setup(self.walls,self.enemies,self.player)

        # Crear la cámara usando el tamaño de la pantalla y del mapa
        map_width, map_height = self.map.get_pixel_size()
        self.camera = Camera(self.width, self.height, map_width, map_height)

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

            # Actualizar la cámara para que siga al primer jugador
            for player in self.players:
                self.camera.update(player)
                break  # Solo seguimos al primer jugador

            self.screen.fill(self.backgroundColor)

            # Dibujar todos los sprites aplicando el offset de la cámara
            for sprite in self.walls:
                self.screen.blit(sprite.image, self.camera.apply(sprite))
            for sprite in self.enemies:
                self.screen.blit(sprite.image, self.camera.apply(sprite))
            for sprite in self.players:
                self.screen.blit(sprite.image, self.camera.apply(sprite))

            if self.player.checkenemycolision(self.enemies):
                self.running = False

            #actulizamos la ventana
            pygame.display.flip()

            #los frames por segundo     
            self.clock.tick (60)

        

        