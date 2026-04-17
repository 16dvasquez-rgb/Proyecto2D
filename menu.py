import pygame

class Button():
    """
    Clase para crear botones interactivos en los menús.
    Cada botón tiene un texto, posición, colores y una acción asociada.
    """
    def __init__(self, text, x, y, width, height, action=None,
                 color=(70, 130, 180), hover_color=(100, 160, 210),
                 text_color=(255, 255, 255), font_size=30, border_radius=10):
        
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.action = action  # función que se ejecuta al hacer click
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.font = pygame.font.SysFont("Arial", font_size, bold=True)
        self.border_radius = border_radius
        self.is_hovered = False

    def draw(self, surface):
        """Dibuja el botón en la superficie dada, cambiando color si el mouse está encima."""
        # Elegir color según si el mouse está encima o no
        current_color = self.hover_color if self.is_hovered else self.color

        # Dibujar el rectángulo del botón con bordes redondeados
        pygame.draw.rect(surface, current_color, self.rect, border_radius=self.border_radius)

        # Dibujar un borde alrededor del botón
        pygame.draw.rect(surface, (255, 255, 255), self.rect, width=2, border_radius=self.border_radius)

        # Renderizar el texto centrado en el botón
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        """Verifica si el mouse está sobre el botón."""
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def check_click(self, mouse_pos):
        """Verifica si se hizo click en el botón y ejecuta su acción."""
        if self.rect.collidepoint(mouse_pos) and self.action:
            self.action()
            return True
        return False


class Label():
    """
    Clase para mostrar textos en los menús.
    Puede ser un título, subtítulo, o cualquier texto decorativo.
    """
    def __init__(self, text, x, y, font_size=50, color=(255, 255, 255),
                 bold=True, font_name="Arial", center=True):
        
        self.text = text
        self.font = pygame.font.SysFont(font_name, font_size, bold=bold)
        self.color = color
        self.center = center  # si True, x e y son el centro del texto

        # Renderizar el texto
        self.surface = self.font.render(self.text, True, self.color)
        
        if self.center:
            self.rect = self.surface.get_rect(center=(x, y))
        else:
            self.rect = self.surface.get_rect(topleft=(x, y))

    def draw(self, surface):
        """Dibuja el texto en la superficie dada."""
        surface.blit(self.surface, self.rect)

    def update_text(self, new_text):
        """Permite cambiar el texto dinámicamente (útil para puntajes, tiempos, etc.)."""
        self.text = new_text
        self.surface = self.font.render(self.text, True, self.color)
        old_center = self.rect.center
        if self.center:
            self.rect = self.surface.get_rect(center=old_center)
        else:
            self.rect = self.surface.get_rect(topleft=self.rect.topleft)


class Menu():
    """
    Clase base para crear menús reutilizables.
    Un menú contiene botones, textos (labels) y un fondo.
    Se puede usar para menú principal, game over, pausa, selección de nivel, etc.
    
    Ejemplo de uso:
        menu = Menu(screen, background_color=(20, 20, 40))
        menu.add_label("MI JUEGO", screen_w // 2, 100, font_size=72)
        menu.add_button("Jugar", screen_w // 2 - 100, 250, 200, 50, action=iniciar_juego)
        menu.add_button("Salir", screen_w // 2 - 100, 320, 200, 50, action=salir)
        
        resultado = menu.run()
    """
    def __init__(self, screen, background_color=(20, 20, 40), background_image=None):
        
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.background_color = background_color
        self.background_image = None
        self.buttons = []
        self.labels = []
        self.running = False
        self.result = None  # almacena el resultado del menú (útil para saber qué opción se eligió)
        self.clock = pygame.time.Clock()

        # Si se proporcionó una imagen de fondo, cargarla y escalarla
        if background_image:
            try:
                img = pygame.image.load(background_image).convert()
                self.background_image = pygame.transform.scale(img, (self.width, self.height))
            except pygame.error:
                self.background_image = None

    def add_button(self, text, x, y, width, height, action=None,
                   color=(70, 130, 180), hover_color=(100, 160, 210),
                   text_color=(255, 255, 255), font_size=30, border_radius=10):
        """Agrega un botón al menú y lo devuelve."""
        button = Button(text, x, y, width, height, action,
                       color, hover_color, text_color, font_size, border_radius)
        self.buttons.append(button)
        return button

    def add_label(self, text, x, y, font_size=50, color=(255, 255, 255),
                  bold=True, font_name="Arial", center=True):
        """Agrega un texto/label al menú y lo devuelve."""
        label = Label(text, x, y, font_size, color, bold, font_name, center)
        self.labels.append(label)
        return label

    def draw_background(self):
        """Dibuja el fondo del menú (color sólido o imagen)."""
        if self.background_image:
            self.screen.blit(self.background_image, (0, 0))
        else:
            self.screen.fill(self.background_color)

    def draw(self):
        """Dibuja todos los elementos del menú."""
        self.draw_background()

        # Dibujar todos los labels
        for label in self.labels:
            label.draw(self.screen)

        # Dibujar todos los botones
        for button in self.buttons:
            button.draw(self.screen)

        pygame.display.flip()

    def handle_events(self):
        """Maneja los eventos del menú (clicks, hover, cerrar ventana)."""
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            # Cerrar ventana
            if event.type == pygame.QUIT:
                self.result = "quit"
                self.running = False
                return

            # Tecla ESC para salir del menú
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.result = "quit"
                    self.running = False
                    return

            # Click del mouse
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in self.buttons:
                    button.check_click(mouse_pos)

        # Actualizar estado hover de todos los botones
        for button in self.buttons:
            button.check_hover(mouse_pos)

    def run(self):
        """
        Ejecuta el bucle principal del menú.
        Retorna self.result cuando el menú se cierra.
        """
        self.running = True
        self.result = None

        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(60)

        return self.result

    def stop(self, result=None):
        """Detiene el menú y guarda un resultado opcional."""
        self.result = result
        self.running = False
