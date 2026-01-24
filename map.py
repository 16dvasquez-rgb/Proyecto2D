class Map:
    def __init__(self,tile_size=50):
        self.content = [
            "WWWWWWWWWW", #[0,0]
            "W P      W", #[1,2]
            "W  EW W  W",
            "W   W W  W",
            "W   W W  W",
            "W   W W  W",
            "W    W   W",
            "W   W W  W",
            "W   W W  W",
            "W        W",
            "WWWWWWWWWW",
        ]
    def setup(self,wall_group,enemy_group,player_group):
        for row_index,row in enumerate(self.content):
            for col_index,col in enumerate(row):
                x = col_index*self.tile_size
                y = row_index*self.tile_size
                print("Fix Release")
                print("Fix Release 2")
                

