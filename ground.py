import pygame
from tiles import Tile
from mapp import tile_size

class Ground:
    def __init__(self,ground_data,ground_result):
        self.display_ground= ground_result
        self.setup_ground(ground_data)

    def setup_ground (self,layout):

        self.tiles=pygame.sprite.Group()

        for row_index,row in enumerate(layout):#index and information
             for col_index,lock in enumerate(row):
                 if lock == 'X':
                     x = col_index * tile_size
                     y = row_index * tile_size
                     tile = Tile((x,y),tile_size)#x and y as pos
                     self.tiles.add(tile)

    def run(self):
        self.tiles.draw(self.display_ground)
         