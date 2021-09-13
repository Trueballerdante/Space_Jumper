from View.pause_view import pause_menu
import pygame, sys
from Model.player_class import player_
from Model.obstacles.spike_obstacle import spike
from Model.obstacles.platform_class import platform
from Controller.collisions import *
from Controller.timer_class import timer
from Model.text_class import text
from Model.button_class import button

class level_2():
    def __init__(self, screen):
        self.screen = screen
        self.starting_position = (50, 500)
        #Create player
        self.p = player_("View/players/ufo.png", self.starting_position, 3, 15, 500)
        self.player = pygame.sprite.GroupSingle()
        self.player.add(self.p)
        self.font = "Times New Roman"
        self.timer = timer()

        #timer text
        self.time_text = text("Time: ", self.font, 40, (60, 20), "White")

        #create spikes
        self.spike1 = spike((550, 500))
        self.spike2 = spike((520, 500))
        self.spike3 = spike((275, 400))
        self.spike4 = spike((650, 500))
        self.spike5 = spike((700, 500))
        self.spike6 = spike((750, 500))
        self.spike7 = spike((800, 500))
        self.spike8 = spike((850, 500))
        self.spikes = pygame.sprite.Group()
        self.spikes.add(self.spike1, self.spike2, self.spike3, self.spike4, self.spike5, self.spike6, self.spike7, self.spike8)

        #Create ground platforms
        self.platform1 = platform((100, 470, 50, 30), (200, 200, 200))
        self.platform2 = platform((200, 400, 150, 30), (200, 200, 200))
        self.platform3 = platform((440, 350, 50, 150), (200, 200, 200))
        self.platform4 = platform((580, 350, 50, 150), (200, 200, 200))
        self.platform5 = platform((700, 300, 115, 10), (200, 200, 200))
        self.platform6 = platform((900, 250, 100, 250), (200, 200, 200))
        self.platforms = [self.platform1, self.platform2, self.platform3, self.platform4, self.platform5 ,self.platform6] 

        #Create pause button
        self.pause_button = button("Pause", self.font, 40, (930, 40), "Black")

    def run(self):
        self.screen.fill((134, 79, 230))

        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 500, 1000, 100))

        #Manage Spikes
        self.spikes.draw(self.screen)
        spike_collision(self.spikes.sprites(), self.player.sprite, self.starting_position)

        #Manage Ground platforms
        for platform in self.platforms:
            pygame.draw.rect(self.screen, platform.color, platform)
        platform_collision(self.player.sprite, self.platforms)

        #manage time
        new_text = "Time: " + str(self.timer.get_time())
        self.time_text.update_text(new_text)
        self.time_text.display_text(self.screen)

        #display pause button
        self.pause_button.display_button(self.screen, (102, 178, 255))
        
        self.player.draw(self.screen)
        self.player.update()

        if self.player.sprite.rect.left >= 1000:
            #reset the players position before switching to the next level
            self.player.sprite.reset_position(self.starting_position)
            return "level_three"
        elif self.pause_button.check_if_clicked():
            pause_menu.paused_level = "level_two"
            return "pause_menu"
        else:
            return "level_two"