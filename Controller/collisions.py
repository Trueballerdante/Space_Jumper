import pygame
from pygame.constants import K_LEFT, K_RIGHT, K_UP

def spike_collision(spikes, player, starting_position):
    if pygame.sprite.spritecollideany(player, spikes):
        player.reset_position(starting_position)
        player.reset_gravity()

#platform_type: 0 = regular, 1 = moving_horizontal, 2  moving_vertical
def platform_collision(player, platforms, platform_type=0):

    collision_tolerance = 5
    collision_tolerance_top = 15 #15 because of the gravity factor
    collision_tolerance_bottom = 15
    for platform in platforms:
        if player.rect.colliderect(platform.rect):

            #check for left collision
            if abs(player.rect.right - platform.rect.left) < collision_tolerance:
                player.rect.right = platform.rect.left
            
            #check for right collision
            elif abs(player.rect.left - platform.rect.right) < collision_tolerance:
                player.rect.left = platform.rect.right

            #check for top collision
            elif abs(player.rect.bottom - platform.rect.top) < collision_tolerance_top:
                player.on_platform = True
                platform.player_on_top = True
                # + 1 because Returns true if any portion of either rectangle overlap 
                # (except the top+bottom or left+right edges).
                player.rect.bottom = platform.rect.top + 1

                #move player with horizontal moving platform
                if platform_type == 1:
                    if platform.is_moving_right:
                        player.rect.x += platform.speed
                    else:
                        player.rect.x -= platform.speed
                
                if platform_type == 2:
                    if platform.is_moving_up:
                        player.rect.y -= platform.speed
                    else:
                        player.rect.y += platform.speed

                player.in_air = False
                player.reset_gravity()
            
            #check for bottom collision
            elif abs(player.rect.top - platform.rect.bottom) < collision_tolerance_bottom:
                #make sure player is not in the platform due to the collision_tolerance. then reverse the direction
                #of the gravity
                player.rect.top = platform.rect.bottom
                player.gravity *= -1
            

        elif platform.player_on_top == True:
            platform.player_on_top = False
            player.on_platform = False
            player.in_air = True

def lava_collision(lava_pools, player, starting_position):
    for lava in lava_pools:
        if player.rect.colliderect(lava.rect):
            player.reset_position(starting_position)
            player.reset_gravity()
