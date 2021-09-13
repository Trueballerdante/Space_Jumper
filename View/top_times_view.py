from View.game_over_class import game_over
from Controller.database.manage_top_time_database import get_all
import pygame
import sys
from Model.button_class import button
from Model.text_class import text

class top_times():
    def __init__(self, screen):
        self.screen = screen
        self.font = "Times New Roman"

        #Create main menu button
        self.main_menu_button = button("Main Menu", self.font, 40, (880, 50), "Black")

        #Create top times text
        self.top_times_text = text("Top Times", self.font, 70, (500, 50), "Black")

        #Create times texts
        self.time1 = text("", self.font, 60, (100, 150), "Black")
        self.time2 = text("", self.font, 60, (100, 250), "Black")
        self.time3 = text("", self.font, 60, (100, 350), "Black")
        self.time4 = text("", self.font, 60, (100, 450), "Black")
        self.time5 = text("", self.font, 60, (100, 550), "Black")
        self.times = [self.time1, self.time2, self.time3, self.time4, self.time5]

    def run(self):
        self.screen.fill((0, 153, 76))

        self.top_times_text.display_text(self.screen)

        self.main_menu_button.display_button(self.screen, (102, 178, 255))

        index = 0
        for record in get_all():
            self.times[index].update_text(str(record[0]) + ".) " + record[1] + ": " + str(record[2]) + " seconds")
            self.times[index].display_text(self.screen)
            index += 1

        #check if button is pressed
        if self.main_menu_button.check_if_clicked():
            return "main_menu"
        else: 
            return "top_times"

