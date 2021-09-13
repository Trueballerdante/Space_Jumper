import pygame
import sys
from Model.button_class import button
from Model.text_class import text
from View.game_over_class import game_over

class menu():
    def __init__(self, screen):
        self.screen = screen
        self.font = "Times New Roman"

        #Create start game button
        self.start_game_button = button("Start Game", self.font, 40, (500, 300), "Black")
        #create view top times button
        self.view_times_button = button("View Top Times", self.font, 40, (500, 370), "Black")

        #Create title text
        self.title_text = text("Space Jumper", self.font, 70, (500, 200), "Black")

        self.creator_name_text = text("Created by: Dante Garcia", self.font, 30, (160, 580), "Black")

    def run(self):
        self.screen.fill((0, 153, 76))

        self.title_text.display_text(self.screen)

        self.start_game_button.display_button(self.screen, (102, 178, 255))
        self.view_times_button.display_button(self.screen, (102, 178, 255))

        self.creator_name_text.display_text(self.screen)

        #check if button is pressed
        if self.start_game_button.check_if_clicked():
            return "level_one"
        elif self.view_times_button.check_if_clicked():
            return "top_times"
        else: 
            return "main_menu"

