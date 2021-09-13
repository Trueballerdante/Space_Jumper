import pygame
from Model.obstacles.platform_class import platform

class moving_platform_h(platform):
    def __init__(self, location, color, speed, left_bound, right_bound):
        super().__init__(location, color)
        self.speed = speed
        self.r_bound = right_bound
        self.l_bound = left_bound
        self.is_moving_right = True
        self.tolerance = 5

    def move_platform(self):
        if abs(self.l_bound - self.rect.left) <= 5:
            self.rect.right += self.speed
            self.is_moving_right = True
        elif abs(self.r_bound - self.rect.right) <= 5:
            self.rect.right -= self.speed
            self.is_moving_right = False
        else:
            if self.is_moving_right:
                self.rect.right += self.speed
            else:
                self.rect.right -= self.speed