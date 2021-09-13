import pygame

#Spike icon made by Freepik from www.flaticon.com

class spike(pygame.sprite.Sprite):
    def __init__(self, location):
        super().__init__()
        self.location = location
        self.image = pygame.image.load("View/obstacle_pics/spike.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = self.location)