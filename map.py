from wall import Wall
from player import Player
from enemy import Enemy

class Map:
    def __init__(self,tile_size=50):
        self.content = [
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
            "W                            W",
            "W  EW W       W   W     E    W",
            "W   W W       W   W          W",
            "W   W W       W   WWWWW      W",
            "W   W W       W         E    W",
            "W    W        W   WWWWW      W",
            "W   W W       W   W          W",
            "W   W W       W   W          W",
            "W        WWWWWW   W          W",
            "W            P    W          W",
            "W   WWWWW         WWWWWWWW   W",
            "W       W                    W",
            "W       W    E    W          W",
            "W       W         W   WWWW   W",
            "W   E   WWWWWW    W          W",
            "W                 W          W",
            "W   WWWWW    W    W   E      W",
            "W            W               W",
            "W       E    W    WWWWWWWW   W",
            "W            W               W",
            "W   WWWWWWWWWW         E     W",
            "W                            W",
            "W     E          WWWWWW      W",
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
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
                    enemy = Enemy(x,y,15)
                    enemy_group.add(enemy)
                elif col == "P":
                    player = Player (x,y,15)
                    player_group.add(player)
