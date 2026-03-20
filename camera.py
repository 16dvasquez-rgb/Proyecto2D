import pygame

class Camera:
    """
    Clase que representa la cámara del juego.
    
    La cámara sigue a un objetivo (normalmente el jugador) y calcula
    un offset que se usa para desplazar todos los sprites al dibujarlos.
    Esto permite tener mapas más grandes que la pantalla.
    
    Atributos:
        offset_x (int): Desplazamiento horizontal de la cámara
        offset_y (int): Desplazamiento vertical de la cámara
        screen_width (int): Ancho de la pantalla en píxeles
        screen_height (int): Alto de la pantalla en píxeles
        map_width (int): Ancho total del mapa en píxeles
        map_height (int): Alto total del mapa en píxeles
    """

    def __init__(self, screen_width, screen_height, map_width, map_height):
        """
        Inicializa la cámara.

        Args:
            screen_width (int): Ancho de la pantalla
            screen_height (int): Alto de la pantalla
            map_width (int): Ancho total del mapa en píxeles
            map_height (int): Alto total del mapa en píxeles
        """
        self.offset_x = 0
        self.offset_y = 0
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.map_width = map_width
        self.map_height = map_height

    def update(self, target):
        """
        Actualiza la posición de la cámara para centrarla en el objetivo.
        
        Usa 'clamp' para asegurarse de que la cámara no se salga
        de los límites del mapa (no muestra espacio vacío).

        Args:
            target (pygame.sprite.Sprite): El sprite que la cámara debe seguir
        """
        # Calculamos el offset para centrar el objetivo en la pantalla
        self.offset_x = target.rect.centerx - self.screen_width // 2
        self.offset_y = target.rect.centery - self.screen_height // 2

        # Clamp: no dejar que la cámara se salga de los bordes del mapa
        # Si el offset es negativo, significa que estamos antes del inicio del mapa
        if self.offset_x < 0:
            self.offset_x = 0
        # Si el offset + pantalla es mayor que el mapa, estamos pasando el final
        if self.offset_x > self.map_width - self.screen_width:
            self.offset_x = self.map_width - self.screen_width

        if self.offset_y < 0:
            self.offset_y = 0
        if self.offset_y > self.map_height - self.screen_height:
            self.offset_y = self.map_height - self.screen_height

    def apply(self, sprite):
        """
        Aplica el offset de la cámara a un sprite.
        
        Retorna un nuevo rect con la posición ajustada para dibujar
        el sprite en la posición correcta de la pantalla.

        Args:
            sprite (pygame.sprite.Sprite): El sprite al que aplicar el offset

        Returns:
            pygame.Rect: El rect del sprite desplazado por el offset de la cámara
        """
        return sprite.rect.move(-self.offset_x, -self.offset_y)
