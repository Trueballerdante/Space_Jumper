import pygame

class text():
    def __init__(self, text, font, font_size, location, color):
        self.font = pygame.font.SysFont(font, font_size)
        self.color = color
        self.text = self.font.render(text, True, color)
        self.rect = self.text.get_rect(center = location)
    
    def display_text(self, screen): 
        screen.blit(self.text, self.rect)

    def update_text(self, text):
        self.text = self.font.render(text, True, self.color)
