from View.pause_view import pause_menu
import pygame, sys
from Model.player_class import player_
from Model.obstacles.spike_obstacle import spike
from Model.obstacles.platform_class import platform
from Model.obstacles.moving_platform_vertical import moving_platform_v
from Model.obstacles.lava_class import lava_pool
from Controller.collisions import *
from Controller.timer_class import timer
from Model.text_class import text
from Model.button_class import button

class level_6():
    def __init__(self, screen):
        self.screen = screen
        #self.starting_position = (900, 500) #testing position 
        self.starting_position = (0 + 16, 171)
        #Create player
        self.p = player_("View/players/ufo.png", self.starting_position, 3, 15, 500)
        self.player = pygame.sprite.GroupSingle()
        self.player.add(self.p)
        self.font = "Times New Roman"
        self.timer = timer()

        #timer text
        self.time_text = text("Time: ", self.font, 40, (60, 20), "White")

        #create spikes
        #row 1
        self.spike1 = spike((100 + 16, 170))
        #self.spike2 = spike((200 + 16, 170))
        self.spike2 = spike((300 + 16, 170))
        #self.spike4 = spike((400 + 16, 170))
        self.spike3 = spike((500 + 16, 170))
        #self.spike6 = spike((600 + 16, 170))
        self.spike4 = spike((700 + 16, 170))
        #self.spike8 = spike((800 + 16, 170))
        #row 2
        self.spike5 = spike((850 - 16, 330))
        #self.spike10 = spike((750 - 16, 330))
        self.spike6 = spike((650 - 16, 330))
        #self.spike12 = spike((550 - 16, 330))
        self.spike7 = spike((450 - 16, 330))
        #self.spike14 = spike((350 - 16, 330))
        self.spike8 = spike((250 - 16, 330))
        #self.spike16 = spike((150 - 16, 330))
        #row 3
        self.spike9 = spike((100 + 16, 500))
        #self.spike18 = spike((200 + 16, 500))
        self.spike10 = spike((300 + 16, 500))
        #self.spike20 = spike((400 + 16, 500))
        self.spike11 = spike((500 + 16, 500))
        #self.spike22 = spike((600 + 16, 500))
        self.spike12 = spike((700 + 16, 500))
        #self.spike24 = spike((800 + 16, 500))

        self.spikes = pygame.sprite.Group()
        self.spikes.add(self.spike1, self.spike2, self.spike3, self.spike4, self.spike5,
                        self.spike6, self.spike7, self.spike8, self.spike9, self.spike10,
                        self.spike11, self.spike12)

        #Create platforms
        self.platform1 = platform((0, 0, 1000, 20), (3, 57, 166))
        self.platform2 = platform((0, 170, 920, 20), (3, 57, 166))
        self.platform3 = platform((50, 330, 1000, 20), (3, 57, 166))
        self.platform4 = platform((980, 20, 20, 330), (3, 57, 166))
        self.platforms = [self.platform1, self.platform2, self.platform3, self.platform4] 

        #Create pause button
        self.pause_button = button("Pause", self.font, 40, (930, 40), "Black")


    def run(self):
        self.screen.fill((86, 214, 212))

        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 500, 1000, 100))

        #Manage Spikes
        self.spikes.draw(self.screen)
        spike_collision(self.spikes.sprites(), self.player.sprite, self.starting_position)

        #Manage platforms
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
            return "game_over"
        elif self.pause_button.check_if_clicked():
            pause_menu.paused_level = "level_six"
            return "pause_menu"
        else:
            return "level_six"