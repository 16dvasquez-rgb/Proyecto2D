import pygame
from map import Map
from camera import Camera
from menu import Menu

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
        self.caption = caption
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()

    def _setup_game(self):
        """Inicializa todos los elementos del juego (mapa, sprites, cámara)."""
        self.running = True
        self.players = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.map = Map()
        self.map.setup(self.walls,self.enemies,self.players)

        # Crear la cámara usando el tamaño de la pantalla y del mapa
        map_width, map_height = self.map.get_pixel_size()
        self.camera = Camera(self.width, self.height, map_width, map_height)

    def _create_main_menu(self):
        """Crea y configura el menú principal del juego."""
        menu = Menu(self.screen, background_color=(15, 15, 35))

        # Título del juego
        menu.add_label("MI JUEGO", self.width // 2, self.height // 4,
                       font_size=80, color=(255, 215, 0))

        # Subtítulo
        menu.add_label("Presiona un botón para continuar",
                       self.width // 2, self.height // 4 + 70,
                       font_size=22, color=(180, 180, 200))

        # Botón Jugar
        btn_w, btn_h = 250, 60
        btn_x = self.width // 2 - btn_w // 2

        menu.add_button("Jugar", btn_x, self.height // 2, btn_w, btn_h,
                        action=lambda: menu.stop("play"),
                        color=(34, 139, 34), hover_color=(50, 180, 50))

        # Botón Salir
        menu.add_button("Salir", btn_x, self.height // 2 + 80, btn_w, btn_h,
                        action=lambda: menu.stop("quit"),
                        color=(178, 34, 34), hover_color=(220, 60, 60))

        return menu

    def _create_game_over_menu(self):
        """Crea y configura la pantalla de Game Over."""
        menu = Menu(self.screen, background_color=(40, 10, 10))

        # Texto Game Over
        menu.add_label("GAME OVER", self.width // 2, self.height // 4,
                       font_size=90, color=(220, 20, 60))

        menu.add_label("¡Has sido atrapado!", self.width // 2, self.height // 4 + 80,
                       font_size=28, color=(200, 150, 150))

        btn_w, btn_h = 250, 60
        btn_x = self.width // 2 - btn_w // 2

        # Botón Reintentar
        menu.add_button("Reintentar", btn_x, self.height // 2 + 20, btn_w, btn_h,
                        action=lambda: menu.stop("retry"),
                        color=(34, 139, 34), hover_color=(50, 180, 50))

        # Botón Menú Principal
        menu.add_button("Menú Principal", btn_x, self.height // 2 + 100, btn_w, btn_h,
                        action=lambda: menu.stop("menu"),
                        color=(70, 130, 180), hover_color=(100, 160, 210))

        # Botón Salir
        menu.add_button("Salir", btn_x, self.height // 2 + 180, btn_w, btn_h,
                        action=lambda: menu.stop("quit"),
                        color=(178, 34, 34), hover_color=(220, 60, 60))

        return menu

    def _run_game(self):
        """Ejecuta el bucle principal del juego (gameplay)."""
        self._setup_game()
        pygame.display.set_caption(self.caption)

        pygame.mixer.music.load("assets/frenzy style.mp3")
        pygame.mixer.music.play(-1)

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
            self.players.update(keys,self.width,self.height,self.walls)
            self.enemies.update(keys,self.width,self.height,self.walls)

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
                if sprite.checkenemycolision(self.enemies):
                    self.running = False


            #actulizamos la ventana
            pygame.display.flip()

            #los frames por segundo     
            self.clock.tick (60)

        # Detener la música al salir del juego
        pygame.mixer.music.stop()

    def run(self):
        """
        Punto de entrada principal de la aplicación.
        Maneja el flujo completo: Menú Principal → Juego → Game Over → repetir.
        """
        app_running = True

        while app_running:
            # --- Menú Principal ---
            resultado = self._create_main_menu().run()

            if resultado == "quit" or resultado is None:
                break

            if resultado == "play":
                # --- Jugar ---
                self._run_game()

                # --- Game Over loop ---
                in_game_over = True
                while in_game_over:
                    resultado_go = self._create_game_over_menu().run()

                    if resultado_go == "retry":
                        self._run_game()

                    elif resultado_go == "menu":
                        in_game_over = False

                    elif resultado_go == "quit" or resultado_go is None:
                        in_game_over = False
                        app_running = False

        pygame.quit()