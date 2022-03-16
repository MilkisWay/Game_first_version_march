import sys
import pygame

#General setup
pygame.init()
clock=pygame.time.Clock()

#Game screen
screen=pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Harry Potter")

#loadimages
background_img=pygame.image.load('background.png')#free
background1_img=pygame.image.load('background1.png')#free
background2_img=pygame.image.load('background2.png')#free
#run=True?
while True:

    screen.blit(background_img,(0,0))
    screen.blit(background1_img,(0,0))
    screen.blit(background2_img,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)
