import pygame, sys
from Model.player_class import player_
from Model.obstacles.spike_obstacle import spike
from Model.obstacles.lava_class import lava_pool
from Model.obstacles.platform_class import platform
from Model.obstacles.moving_platform_horizontal import moving_platform_h
from Model.obstacles.moving_platform_vertical import moving_platform_v
from Controller.collisions import *

class test_l():
    def __init__(self, screen):
        self.screen = screen
        self.starting_position = (16, 101) #used 101 to ensure a collision with the starting platform
        #Create player
        self.p = player_("View/players/ufo.png", self.starting_position, 3, 15, 500)
        self.player = pygame.sprite.GroupSingle()
        self.player.add(self.p)

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
        self.platform1 = platform((100, 470, 50, 30), "Purple")
        self.platform2 = platform((200, 400, 150, 30), "Purple")
        self.platform3 = platform((440, 350, 50, 150), "Purple")
        self.platform4 = platform((580, 350, 50, 150), "Purple")
        self.platform5 = platform((700, 300, 115, 10), "Purple")
        self.platform6 = platform((900, 250, 100, 250), "Purple")
        #self.platforms = [self.platform1, self.platform2, self.platform3, self.platform4, self.platform5 ,self.platform6] 
        self.platform7 = platform((0, 100, 50, 30), "Purple")
        self.platforms = [self.platform7]

        #create moving horizontal platforms
        self.moving_h_platform1 = moving_platform_h((110, 400, 150, 30), "Purple", 1, 50, 300)
        self.moving_h_platforms = [self.moving_h_platform1]

        #create moving vertical platforms
        self.moving_v_platform1 = moving_platform_v((400, 200, 50, 30), "Purple", 2, 100, 450)
        self.moving_v_platforms = [self.moving_v_platform1]

        #create lava pools
        self.lava_pool1 = lava_pool((500, 495, 50, 20))
        self.lava_pools = [self.lava_pool1]


    def run(self):
        self.screen.fill((30, 212, 123))

        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 500, 1000, 100))

        #Manage Spikes
        #self.spikes.draw(self.screen)
        #spike_collision(self.spikes.sprites(), self.player.sprite, self.starting_position)

        #Manage Ground platforms
        for platform in self.platforms:
           pygame.draw.rect(self.screen, platform.color, platform)
        platform_collision(self.player.sprite, self.platforms)
        
        #manage moving horizontal platforms
        for platform in self.moving_h_platforms:
            platform.move_platform()
            pygame.draw.rect(self.screen, platform.color, platform)
        platform_collision(self.player.sprite, self.moving_h_platforms, 1)

        #manage moving vertical platforms
        for platform in self.moving_v_platforms:
            platform.move_platform()
            pygame.draw.rect(self.screen, platform.color, platform)
        platform_collision(self.player.sprite, self.moving_v_platforms, 2)

        #manage lava pools
        for lava in self.lava_pools:
            pygame.draw.rect(self.screen, lava.color, lava)
        lava_collision(self.lava_pools, self.player.sprite, self.starting_position)
        


        self.player.draw(self.screen)
        self.player.update()

        return "test_level"