import sys
import pygame
from pygame.constants import DOUBLEBUF, FULLSCREEN, HWSURFACE, K_ESCAPE
from mapp import *
from ground import *
#General setup
pygame.init()
clock=pygame.time.Clock()

#Game screen
screen=pygame.display.set_mode((screen_width,screen_height),HWSURFACE|DOUBLEBUF,32) #add FULLSCREAN, works
pygame.display.set_caption("Harry Potter")
ground = Ground(surface_map,screen)

#loadimages
background_img=pygame.image.load('Background1.jpg')
#background1_img=pygame.image.load('background1.png')#free
#background2_img=pygame.image.load('background2.png')#free
#run=True?
while True:

    screen.blit(background_img,(0,0))
    #screen.blit(background1_img,(0,0))
    #screen.blit(background2_img,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    #screen.fill('black')
    ground.run()
    pygame.display.update()
    clock.tick(60)
