from pygame.constants import K_a
from Controller.database.manage_top_time_database import *
import pygame
import sys
from Model.button_class import button
from Model.text_class import text
from View.game_over_class import game_over

class add_time():
    def __init__(self, screen):
        self.screen = screen
        self.font = "Times New Roman"
        self.name = ""
        self.letter_typed = False
        self.backspace_typed = False

        #Create save button
        self.save_button = button("Save", self.font, 50, (930, 50), "Black")

        #Create congratulations text
        self.congrats_text = text("Congratulations!", self.font, 70, (500, 150), "Black")

        #create placement text
        self.placement_text = text("", self.font, 50, (350, 250), "Black")

        #time text
        self.time_text = text("", self.font, 70, (250, 50), "Black")

        #user input text
        self.user_name = text("", self.font, 50, (300, 350), "Black")


    def run(self):
        self.screen.fill((0, 153, 76))

        self.time_text.update_text("Final Time: " + str(game_over.final_time))
        self.time_text.display_text(self.screen)

        self.congrats_text.display_text(self.screen)

        self.placement_text.update_text("You placed " + get_placement(game_over.final_time))
        self.placement_text.display_text(self.screen)

        keys = pygame.key.get_pressed()
        self.get_name(keys)
        self.user_name.update_text("Enter three letters: " + self.name)
        self.user_name.display_text(self.screen)

        self.save_button.display_button(self.screen, (102, 178, 255))

            
        #check if button is pressed
        if self.save_button.check_if_clicked():
            self.letter_typed = False
            self.backspace_typed = False
            add_new_time(self.name, game_over.final_time)
            self.name = ""
            return "game_over"
        else: 
            return "add_time"


    def get_name(self, keys):
        if len(self.name) < 3 or keys[pygame.K_BACKSPACE]:
            if keys[pygame.K_a]:
                if not self.letter_typed:
                    self.name += "A"
                    self.letter_typed = True
            elif keys[pygame.K_b]:
                if not self.letter_typed:
                    self.name += "B"
                    self.letter_typed = True
            elif keys[pygame.K_c]:
                if not self.letter_typed:
                    self.name += "C"
                    self.letter_typed = True
            elif keys[pygame.K_d]:
                if not self.letter_typed:
                    self.name += "D"
                    self.letter_typed = True
            elif keys[pygame.K_e]:
                if not self.letter_typed:
                    self.name += "E"
                    self.letter_typed = True
            elif keys[pygame.K_f]:
                if not self.letter_typed:
                    self.name += "F"
                    self.letter_typed = True
            elif keys[pygame.K_g]:
                if not self.letter_typed:
                    self.name += "G"
                    self.letter_typed = True
            elif keys[pygame.K_h]:
                if not self.letter_typed:
                    self.name += "H"
                    self.letter_typed = True
            elif keys[pygame.K_i]:
                if not self.letter_typed:
                    self.name += "I"
                    self.letter_typed = True
            elif keys[pygame.K_j]:
                if not self.letter_typed:
                    self.name += "J"
                    self.letter_typed = True
            elif keys[pygame.K_k]:
                if not self.letter_typed:
                    self.name += "K"
                    self.letter_typed = True
            elif keys[pygame.K_l]:
                if not self.letter_typed:
                    self.name += "L"
                    self.letter_typed = True
            elif keys[pygame.K_m]:
                if not self.letter_typed:
                    self.name += "M"
                    self.letter_typed = True
            elif keys[pygame.K_n]:
                if not self.letter_typed:
                    self.name += "N"
                    self.letter_typed = True
            elif keys[pygame.K_o]:
                if not self.letter_typed:
                    self.name += "O"
                    self.letter_typed = True
            elif keys[pygame.K_p]:
                if not self.letter_typed:
                    self.name += "P"
                    self.letter_typed = True
            elif keys[pygame.K_q]:
                if not self.letter_typed:
                    self.name += "Q"
                    self.letter_typed = True
            elif keys[pygame.K_r]:
                if not self.letter_typed:
                    self.name += "R"
                    self.letter_typed = True
            elif keys[pygame.K_s]:
                if not self.letter_typed:
                    self.name += "S"
                    self.letter_typed = True
            elif keys[pygame.K_t]:
                if not self.letter_typed:
                    self.name += "T"
                    self.letter_typed = True
            elif keys[pygame.K_u]:
                if not self.letter_typed:
                    self.name += "U"
                    self.letter_typed = True
            elif keys[pygame.K_v]:
                if not self.letter_typed:
                    self.name += "V"
                    self.letter_typed = True
            elif keys[pygame.K_w]:
                if not self.letter_typed:
                    self.name += "W"
                    self.letter_typed = True
            elif keys[pygame.K_x]:
                if not self.letter_typed:
                    self.name += "X"
                    self.letter_typed = True
            elif keys[pygame.K_y]:
                if not self.letter_typed:
                    self.name += "Y"
                    self.letter_typed = True
            elif keys[pygame.K_z]:
                if not self.letter_typed:
                    self.name += "Z"
                    self.letter_typed = True
            elif keys[pygame.K_BACKSPACE]:
                if not self.backspace_typed:
                    self.name = self.name[0:len(self.name) - 1]
                    self.backspace_typed = True
            else:
                self.name += ""
                self.letter_typed = False
                self.backspace_typed = False
        