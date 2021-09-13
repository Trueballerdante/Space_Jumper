from View.pause_view import pause_menu
import pygame, sys
from Model.player_class import player_
from Model.obstacles.spike_obstacle import spike
from Model.obstacles.platform_class import platform
from Model.obstacles.moving_platform_horizontal import moving_platform_h
from Model.obstacles.moving_platform_vertical import moving_platform_v
from Model.obstacles.lava_class import lava_pool
from Controller.collisions import *
from Controller.timer_class import timer
from Model.text_class import text
from Model.button_class import button

class level_4():
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
        self.spike1 = spike((225, 150))
        self.spikes = pygame.sprite.Group()
        self.spikes.add(self.spike1)

        #Create platforms
        self.platform1 = platform((150, 150, 150, 350), "Green")
        self.platform2 = platform((400, 300, 50, 10), "Green")
        self.platform3 = platform((500, 250, 50, 10), "Green")
        self.platform4 = platform((600, 300, 50, 10), "Green")
        self.platform5 = platform((750, 400, 50, 10), "Green")
        self.platform6 = platform((880, 350, 120, 150), "Green")
        self.platforms = [self.platform1, self.platform2, self.platform3, self.platform4, self.platform5,
                            self.platform6] 

        #Create vertically moving platforms
        self.moving_platform_v1 = moving_platform_v((100, 300, 50, 10), "Green", 2, 150, 460)
        self.moving_platform_v = [self.moving_platform_v1]

        #Create lava pools
        self.lava_pool1 = lava_pool((300, 475, 580, 25))
        self.lava_pools = [self.lava_pool1]

        #Create pause button
        self.pause_button = button("Pause", self.font, 40, (930, 40), "Black")


    def run(self):
        self.screen.fill((12, 62, 58))

        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 500, 1000, 100))

        #Manage Spikes
        self.spikes.draw(self.screen)
        spike_collision(self.spikes.sprites(), self.player.sprite, self.starting_position)

        #Manage platforms
        for platform in self.platforms:
            pygame.draw.rect(self.screen, platform.color, platform)
        platform_collision(self.player.sprite, self.platforms)

        #manage moving vertical platforms
        for platform in self.moving_platform_v:
            pygame.draw.rect(self.screen, platform.color, platform)
            platform.move_platform()
        platform_collision(self.player.sprite, self.moving_platform_v, 2)

        #manage lava pools
        for lava in self.lava_pools:
            pygame.draw.rect(self.screen, lava.color, lava)
        lava_collision(self.lava_pools, self.player.sprite, self.starting_position)

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
            return "level_five"
        elif self.pause_button.check_if_clicked():
            pause_menu.paused_level = "level_four"
            return "pause_menu"
        else:
            return "level_four"