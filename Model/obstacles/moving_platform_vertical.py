import pygame
from Model.obstacles.platform_class import platform

class moving_platform_v(platform):
    def __init__(self, location, color, speed, upper_bound, lower_bound):
        super().__init__(location, color)
        self.speed = speed
        self.u_bound = upper_bound
        self.l_bound = lower_bound
        self.is_moving_up = True
        self.tolerance = 5

    def move_platform(self):
        if abs(self.u_bound - self.rect.top) <= 5:
            self.rect.bottom += self.speed
            self.is_moving_up = False
        elif abs(self.l_bound - self.rect.bottom) <= 5:
            self.rect.bottom -= self.speed
            self.is_moving_up = True
        else:
            if self.is_moving_up:
                self.rect.bottom -= self.speed
            else:
                self.rect.bottom += self.speed