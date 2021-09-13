import pygame

class platform():
    def __init__(self, location, color):
        self.location = location
        self.rect = pygame.Rect(location)
        self.color = color
        self.player_on_top = False
