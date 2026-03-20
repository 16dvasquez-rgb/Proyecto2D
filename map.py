from wall import Wall
from player import Player
from enemy import Enemy

class Map:
    def __init__(self,tile_size=25):
        self.content = [
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", #[0,0]
            "W                                    W", #[1,2]
            "W  E                                 W",
            "W                                    W",
            "W                                    W",
            "W                                    W",
            "W                E                   W",
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
            "W                 E                  W",
            "W                                    W",
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]
        self.content = [
    "       WWWWW       ",
    "     WW     WW     ",
    "    W         W    ",
    "   W           W   ",
    "   W  WW   WW  W   ",
    "  W   WW   WW   W  ",
    "  W   WW   WW   W  ",
    "  W             W  ",
    "  W      P      W  ",
    "  W  W       W  W  ",
    "  W  W       W  W  ",   
    "   W  WWWWWWW  W   ",
    "    W         W    ",
    "     WW     WW     ",  
    "       WWWWW       ",
  ]


        self.content = [
            "                                                        WWWWWWWWWW                                      ",
            "                                                        WWWWWWWWWW                                      ",
            "                                                    WWWW          WWWW                                  ",
            "                                                    WWWW          WWWW                                  ",
            "                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW              WWWW                                  ",
            "                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW              WWWW                                  ",
            "          WWWWWWWWWW                                          WWWW                                      ",
            "          WWWWWWWWWW                                          WWWW                                      ",
            "      WWWWWWW                                                     WWWW                                  ",
            "      WWWWWWW                                                     WWWW                                  ",
            "      WWWW   WWWW                     WWWWWWWWWWW                 WWWW                                  ",
            "      WWWW   WWWW                     WWWWWWWWWWW                 WWWW                                  ",
            "      WWWW                                                        WWWW                                  ",
            "      WWWW                                                        WWWW                                  ",
            "      WWWW                                                        WWWW                                  ",
            "      WWWW                   P                                    WWWW                                  ",
            "      WWWW                                                        WWWW                                  ",
            "      WWWW                                                        WWWW                                  ",
            "      WWWW                                                        WWWW                                  ",
            "      WWWW                                      E                 WWWW                                  ",
            "      WWWW                                                        WWWWWWWWWWWWWWWWWWWWW                 ",
            "      WWWW                                                        WWWWWWWWWWWWWWWWWWWWW                 ",
            "      WWWW                                                        WWWW                 WWWW             ",
            "          WWWWWWWWWW                                       WWWWWWW                                      ",
            "          WWWWWWWWWW                                       WWWWWWW                         WWWW         ",
            "                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW                                WWWW         ",
            "                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW                                WWWW         ",
            "                 WWWW                                                                      WWWW         ",
            "                 WWWW                                                                      WWWW         ",
            "                 WWWW                                                                      WWWW         ",
            "                 WWWW                      E                                               WWWW         ",
            "                 WWWW                                                                      WWWW         ",
            "                 WWWW                                                                      WWWW         ",
            "                    WWWW                                                                   WWWW         ",
            "                    WWWW                                                                   WWWW         ",
            "                    WWWW                                WWWWWWW                        WWWW             ",
            "                    WWWW                                WWWWWWW                        WWWW             ",
            "                 WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW       WWWWWWWWWWWWWWWWWWWWWWWW                  ",
            "                 WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW       WWWWWWWWWWWWWWWWWWWWWWWW                  "
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
                
                

