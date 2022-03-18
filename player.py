import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((64,64))
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft=pos)
        self.direction=pygame.math.Vector2(0,0)
        self.speed = 10

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x =1
        elif keys[pygame.K_LEFT]:
            self.direction.x =-1
        elif keys[pygame.K_UP]:
           self.direction.y =1
        elif keys[pygame.K_DOWN]:
            self.direction.x =-1
        else:
            self.direction.x =0
            self.direction.y =0

    def update(self):
        self.get_input()
        self.rect.x+=self.direction.x*self.speed
        self.rect.y+=self.direction.y*self.speed
