import sys
import pygame
from mapp import *
from ground import *
#General setup
pygame.init()
clock=pygame.time.Clock()

#Game screen
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Harry Potter")
ground = Ground(surface_map,screen)

#loadimages
#background_img=pygame.image.load('background.png')#free
#background1_img=pygame.image.load('background1.png')#free
#background2_img=pygame.image.load('background2.png')#free
#run=True?
while True:

    #screen.blit(background_img,(0,0))
    #screen.blit(background1_img,(0,0))
    #screen.blit(background2_img,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    ground.run()
    pygame.display.update()
    clock.tick(60)
