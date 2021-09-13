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

class level_5():
    def __init__(self, screen):
        self.screen = screen
        self.starting_position = (16, 101)
        #Create player
        self.p = player_("View/players/ufo.png", self.starting_position, 3, 15, 500)
        self.player = pygame.sprite.GroupSingle()
        self.player.add(self.p)
        self.font = "Times New Roman"
        self.timer = timer()

        #timer text
        self.time_text = text("Time: ", self.font, 40, (60, 20), "White")

        #create spikes
        self.spike1 = spike((68 + 16, 300))
        self.spike2 = spike((0 + 16, 500))
        self.spikes = pygame.sprite.Group()
        self.spikes.add(self.spike1, self.spike2)

        #Create platforms
        self.platform1 = platform((0, 100, 50, 30), "Black")
        self.platform2 = platform((100, 0, 50, 450), "Black")
        self.platform3 = platform((68, 300, 32, 30), "Black")
        self.platform4 = platform((800, 475, 100, 25), "Black")
        self.platform5 = platform((450, 470, 30, 30), "Black")
        self.platform6 = platform((900, 450, 100, 50), "Black")
        self.platform7 = platform((450, 150, 20, 30), "Black")
        self.platform8 = platform((580, 200, 20, 30), "Black")
        self.platform9 = platform((710, 250, 20, 30), "Black")
        self.platform10 = platform((840, 300, 20, 30), "Black")
        self.platforms = [self.platform1, self.platform2, self.platform3, self.platform4,
                        self.platform5, self.platform6, self.platform7, self.platform8, self.platform9,
                        self.platform10] 

        #creat moving vertical platforms
        self.moving_platform_v1 = moving_platform_v((300, 400, 100, 30), "Black", 3, 100, 460)
        self.moving_platforms_v = [self.moving_platform_v1]

        #create lava pools
        self.lava_pool1 = lava_pool((480, 475, 420, 25))
        self.lava_pools = [self.lava_pool1]

        #Create pause button
        self.pause_button = button("Pause", self.font, 40, (930, 40), "Black")


    def run(self):
        self.screen.fill((116, 129, 150))

        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 500, 1000, 100))

        #Manage Spikes
        self.spikes.draw(self.screen)
        spike_collision(self.spikes.sprites(), self.player.sprite, self.starting_position)

        #Manage platforms
        for platform in self.platforms:
            pygame.draw.rect(self.screen, platform.color, platform)
        platform_collision(self.player.sprite, self.platforms)

        #manage moving vertical platforms
        for platform in self.moving_platforms_v:
            pygame.draw.rect(self.screen, platform.color, platform)
            platform.move_platform()
        platform_collision(self.player.sprite, self.moving_platforms_v, 2)

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
            return "level_six"
        elif self.pause_button.check_if_clicked():
            pause_menu.paused_level = "level_five"
            return "pause_menu"
        else:
            return "level_five"