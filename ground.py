import pygame
from player import Player
from tiles import Tile
from mapp import tile_size, screen_width, screen_height

class Ground:
    def __init__(self,ground_data,ground_result):
        #ground setup
        self.display_ground= ground_result
        self.setup_ground(ground_data)
        self.world_shift_x=0
        self.world_shift_y=0

    def setup_ground (self,layout):

        self.tiles=pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index,row in enumerate(layout):#index and information
             for col_index,lock in enumerate(row):
                 x = col_index * tile_size
                 y = row_index * tile_size
                 if lock == 'X':
                     tile = Tile((x,y),tile_size)#x and y as pos
                     self.tiles.add(tile)
                 if lock == 'P':
                     player_sprite = Player((x,y))
                     self.player.add(player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x=player.rect.centerx
        direction_x= player.direction.x
        if player_x < screen_width/4 and direction_x < 0:
            self.world_shift_x = 10
            player.speed = 0
        elif player_x > (screen_width - screen_width/4) and direction_x > 0:
            self.world_shift_x = -10
            player.speed = 0
        else:
            self.world_shift_x = 0
            player.speed = 10

    def scroll_y(self):#Доделать Ааааааа конец
        player = self.player.sprite
        player_y=player.rect.centery
        direction_y= player.direction.y
        if player_y > screen_height/4 and direction_y < 0:
            self.world_shift_y = 10
            player.speed=0
        else:
            self.world_shift_y = 0
            player.speed = 10

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x+=player.direction.x*player.speed
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x <0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.rect.y+=player.direction.y*player.speed
        for sprite in self.tiles.sprites():
           if sprite.rect.colliderect(player.rect):
               if player.direction.y <0:
                   player.rect.top = sprite.rect.bottom
               elif player.direction.y > 0:
                   player.rect.bottom = sprite.rect.top

    def run(self):

        #tiles
        self.tiles.update(self.world_shift_x,self.world_shift_y)
        self.tiles.draw(self.display_ground)
        self.scroll_x()
        #self.scroll_y()

        #player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_ground)
        
        #self.scroll_y()