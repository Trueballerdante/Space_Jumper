import pygame
import sys
sys.path.append(".")
from Controller.manage_game import game_manager
from pygame import mixer

#game setup
pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Space Jumper")

# Background sound
#https://musiclab.chromeexperiments.com/Song-Maker/song/5287516645621760
mixer.music.load("Controller/Music/main_menu_song.wav")
mixer.music.play(-1) #play in a loop

gm = game_manager(screen)

#create a clock object. We will use this to control the games frame rate
frame_rate = pygame.time.Clock()

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    gm.manage_states()

    pygame.display.update()
    
    frame_rate.tick(60)