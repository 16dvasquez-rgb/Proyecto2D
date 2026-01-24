import pygame

#para que la libreria pygame funcione y todo funcione tambien
pygame.init ()

#para definir las dimensiones (ancho y alto) de la ventana del juego 
WIDTH,HEIGHT = 800,600

WHITE = (255,255,255)
BLUE = (0,0,255)

#para poner la pantalla 
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#para poner el nombre de la ventana 
pygame.display.set_caption ("juego de prueba")

#para controlar los fps del juego
clock = pygame.time.Clock()

#creando un jugador
player_size = 50 
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5


#dice que el juego se esta ejecutando
running = True

#mientras running sea true el juego se ejecuta 
while running:

    #obtenemos y revisamos todos los eventos que se han ejecutado en el juego
    for event in pygame.event.get():

        #aqui validamos si ejecuto el evento de cerrar la ventana (le dimos click a la x)
        if event.type == pygame.QUIT:

            #si se ejecuto el evento de cerrar ventana hacemos que running se igual a false 
            running = False

    #guardar todas las teclas que se presionaron en el juego
    keys = pygame.key.get_pressed()
    if keys [pygame.K_LEFT]:
        player_x -= player_speed
    if keys [pygame.K_RIGHT]:
        player_x += player_speed
    if keys [pygame.K_UP]:
        player_y -= player_speed
    if keys [pygame.K_DOWN]:
        player_y += player_speed

    #volvemos a pintar el fondo del juego
    screen.fill(WHITE)

    pygame.draw.rect(screen,BLUE,(player_x,player_y,player_size,player_size))

    #actulizamos la ventana
    pygame.display.flip()

    #los frames por segundo     
    clock.tick (60)