from Controller.database.manage_top_time_database import *
import pygame
import sys
from Model.button_class import button
from Model.text_class import text
from Controller.timer_class import timer


class game_over():
    final_time = 0
    def __init__(self, screen):
        self.screen = screen
        self.font = "Times New Roman"
        self.timer = timer()
        self.end_of_game = False

        #Create game over text
        self.game_over_text = text("Game Over", self.font, 70, (500, 200), "Black")

        #Create play again button
        self.play_again_button = button("Play Again", self.font, 40, (500, 300), "Black")

        #Create main menu button
        self.main_menu_button = button("Main Menu", self.font, 40, (500, 370), "Black")

    def run(self):
        self.screen.fill((0, 153, 76))

        self.game_over_text.display_text(self.screen)

        self.play_again_button.display_button(self.screen, (102, 178, 255))
        self.main_menu_button.display_button(self.screen, (102, 178, 255))

        if not self.end_of_game:
            #Create time text
            game_over.final_time = self.timer.get_time()
            self.final_time_text = text("Final Time: " + str(game_over.final_time), self.font, 70, (500, 450), "Black")
            if game_over.final_time < get_slowest_time() or get_num_of_records() < 5:
                self.end_of_game = True
                return "add_time"

        self.final_time_text.display_text(self.screen)

        #check if button is pressed
        if self.play_again_button.check_if_clicked():
            self.end_of_game = False
            return "level_one"
        elif self.main_menu_button.check_if_clicked():
            self.end_of_game = False
            return "main_menu"
        else:
            self.end_of_game = True
            self.timer.reset_clock() #The code is being tested here
            return "game_over"
