import pygame

class button():
    def __init__(self, text, font, font_size, location, color):
        self.font = pygame.font.SysFont(font, font_size)
        self.text = self.font.render(text, True, color)
        self.rect = self.text.get_rect(center = location)
    
    def display_button(self, screen, color): 
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, color, self.rect, 10)
        screen.blit(self.text ,self.rect)

    def check_if_clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]: #0 for left mouse button
                return True
            else:
                return False