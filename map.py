from wall import Wall
from player import Player
from enemy import Enemy

class Map:
    def __init__(self,tile_size=100):
        self.content = [
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
            "W                                                                    W",
            "W  P    W   E       W   WWWWWWWWWWW   W   E          W   WWWWWWW     W",
            "W       W           W             W       WWWWWW     W         W     W",
            "W   WWWWW   WWWWW       WWWWWWW   W   WWWWW          W   W     W     W",
            "W       W       W   W         W   W       W   WWWWWWWW   W     W     W",
            "W   W   W   W   W   WWWWW     W   WWWWW   W              W           W",
            "W   W       W   W       W     W       W   W   WWWWWWW   WWWWWWWWW    W",
            "W   WWWWWWWWW   W   W   W E   W   W   W   W         W                W",
            "W               W   W   W     W   W       W   WWWW  W   WWWWW        W",
            "W   WWWWW   WWWWW   W   WWWWWWW   WWWWWWWWW      W  W       W  E     W",
            "W       W              E                          W  W   W   W       W",
            "WWWWW   WWWWWWWWW   WWWWWWWWWWW   WWWWW   WWWWWWWW  W   W   WWWWWWW  W",
            "W           W                 W       W             W   W           EW",
            "W   WWWWW   W   WWWWWWWWWWW   WWWWW   WWWWWWWWWW   WWWWW   WWWWW     W",
            "W       W   W   W     E   W       W          E W               W     W",
            "W   W   W       W   WWWW  W   W   WWWWWWWW     W   WWWWWWWWW   W     W",
            "W   W   WWWWW   W         W   W          W     W   W       W         W",
            "W   W       W   WWWWWWWWWWW   WWWWWW     W   WWWWWWW   E   WWWWW     W",
            "W   WWWWW   W         E           W      W                     W     W",
            "W       W   WWWWWW   WWWWWWWWWW   W  WWWWWWWWW   WWWWWWWWWWW   W     W",
            "W   E   W                     W      W       W               E W     W",
            "W       WWWWWWWWWWW   WWWWW    WWWWWWW   W   WWWWWWWWW   WWWWWWW     W",
            "W                         E                  W                       W",
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]
        self.tile_size = tile_size

    def get_pixel_size(self):
        """
        Retorna el tamaño total del mapa en píxeles (ancho, alto).

        Returns:
            tuple: (ancho_en_pixeles, alto_en_pixeles)
        """
        # El ancho es la fila más larga * tile_size
        max_cols = max(len(row) for row in self.content)
        num_rows = len(self.content)
        return (max_cols * self.tile_size, num_rows * self.tile_size)

    def setup(self,wall_group,enemy_group,player_group):
        for row_index,row in enumerate(self.content):
            for col_index,col in enumerate(row):
                x = col_index*self.tile_size
                y = row_index*self.tile_size
                width = self.tile_size
                height = self.tile_size
                
                if col == "W":
                    wall = Wall(x,y,width,height)
                    wall_group.add(wall)
                elif col == "E":
                    enemy = Enemy(x,y,8)
                    enemy_group.add(enemy)
                elif col == "P":
                    player = Player (x,y,8)
                    player_group.add(player)
