from Controller.timer_class import timer
import pygame
import sys
from Model.button_class import button
from Model.text_class import text
from View.game_over_class import game_over

class pause_menu():
    paused_level = ""
    def __init__(self, screen, levels):
        self.screen = screen
        self.levels = levels
        self.font = "Times New Roman"
        self.paused = False
        self.timer = timer()

        #Create continue game button
        self.continue_button = button("Continue Game", self.font, 40, (500, 300), "Black")
        #create restart button
        self.restart_button = button("Restart", self.font, 40, (500, 440), "Black")
        #create main menu button
        self.main_menu_button = button("Main Menu", self.font, 40, (500, 370), "Black")
        #Create paused text
        self.paused_text = text("Paused", self.font, 70, (500, 100), "Black")
        #Create time text
        self.paused_time_text = text("Current Time: ", self.font, 70, (450, 200), "Black")


    def run(self):
        self.screen.fill((0, 153, 76))

        self.continue_button.display_button(self.screen, (102, 178, 255))
        self.restart_button.display_button(self.screen, (102, 178, 255))
        self.main_menu_button.display_button(self.screen, (102, 178, 255))

        self.paused_text.display_text(self.screen)

        if not self.paused:
            #Create time text
            paused_time = self.timer.get_time()
            self.paused_time_text.update_text("Current Time: " + str(paused_time))

        self.paused_time_text.display_text(self.screen)

        #check if button is pressed
        if self.continue_button.check_if_clicked():
            self.paused = False
            return pause_menu.paused_level
        elif self.restart_button.check_if_clicked():
            self.paused = False
            self.levels[pause_menu.paused_level].player.sprite.reset_position(self.levels[pause_menu.paused_level].starting_position)
            self.timer.reset_clock()
            return "level_one"
        elif self.main_menu_button.check_if_clicked():
            self.paused = False
            self.levels[pause_menu.paused_level].player.sprite.reset_position(self.levels[pause_menu.paused_level].starting_position)
            self.timer.reset_clock()
            return "main_menu"
        else: 
            self.paused = True
            return "pause_menu"
