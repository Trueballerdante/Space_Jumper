from View.pause_view import pause_menu
import pygame, sys
from Model.player_class import player_
from Model.obstacles.spike_obstacle import spike
from Model.obstacles.platform_class import platform
from Model.obstacles.moving_platform_horizontal import moving_platform_h
from Model.obstacles.lava_class import lava_pool
from Controller.collisions import *
from Controller.timer_class import timer
from Model.text_class import text
from Model.button_class import button

class level_3():
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

        #Create ground platforms
        self.platform1 = platform((100, 450, 50, 50), "Purple")
        self.platform2 = platform((150, 400, 50, 100), "Purple")
        self.platform3 = platform((200, 350, 50, 150), "Purple")
        self.platform4 = platform((250, 300, 50, 200), "Purple")
        self.platform5 = platform((300, 250, 50, 250), "Purple")
        self.platform6 = platform((350, 200, 50, 300), "Purple")
        self.platform7 = platform((900, 200, 100, 300), "Purple")
        self.platforms = [self.platform1, self.platform2, self.platform3, self.platform4, self.platform5 ,self.platform6,
                            self.platform7] 

        #create moving horizontal platforms
        self.moving_h_platform1 = moving_platform_h((400, 200, 100, 30), "Purple", 1, 400, 625)
        self.moving_h_platform2 = moving_platform_h((800, 200, 100, 30), "Purple", 1, 675, 900)
        self.moving_h_platforms = [self.moving_h_platform1, self.moving_h_platform2]

        #create lava pools
        self.lava_pool1 = lava_pool((400, 400, 500, 100))
        self.lava_pools = [self.lava_pool1]

        #Create pause button
        self.pause_button = button("Pause", self.font, 40, (930, 40), "Black")


    def run(self):
        self.screen.fill((30, 212, 123))

        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 500, 1000, 100))

        #Manage Ground platforms
        for platform in self.platforms:
            pygame.draw.rect(self.screen, platform.color, platform)
        platform_collision(self.player.sprite, self.platforms)
        
        #manage moving horizontal platforms
        for platform in self.moving_h_platforms:
            pygame.draw.rect(self.screen, platform.color, platform)
            platform.move_platform()
        platform_collision(self.player.sprite, self.moving_h_platforms, 1)
        
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
            return "level_four"
        elif self.pause_button.check_if_clicked():
            pause_menu.paused_level = "level_three"
            return "pause_menu"
        else:
            return "level_three"