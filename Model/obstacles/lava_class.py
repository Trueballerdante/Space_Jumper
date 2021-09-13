import pygame

class lava_pool():
    def __init__(self, location):
        self.location = location
        self.rect = pygame.Rect(location)
        self.color = (207, 16, 32)
