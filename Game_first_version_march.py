import sys
import unit
import pygame 

#General setup
pygame.init()
clock=pygame.time.Clock()

#Game screen
screen=pygame.dispaly.set_mode((1920,1080))
pygame.display.set_caption("Harry Potter")
#run=True?
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    clock.tick(60)
