from wall import Wall
from player import Player
from enemy import Enemy

class Map:
    def __init__(self,tile_size=50):
        self.content = [
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #[0,0]
            "W                                    W", #[1,2]
            "W  E                                 W",
            "W                                    W",
            "W                                    W",
            "W                                    W",
            "W                                    W",
            "W                                    W",
            "W                                    W",
            "W                                    W",
            "W                        P           W",
            "W                                    W",
            "W                                    W",
            "W                                    W",
            "W                                    W",
            "W                                    W",
            "W                                E   W",
            "W                                    W",
            "W                                    W",
            "W                                    W",
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]
        self.tile_size = tile_size
    def setup(self,wall_group,enemy_group,player):
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
                    player.setupPosition(x,y)
                
                

