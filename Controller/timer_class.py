import pygame

class timer():
    #static variables are defined outside of all methods
    time = 0
    start_time = 0
    paused_time = 0
    clock = pygame.time.Clock()
    
    #def start_clock(self):
    #   self.clock.tick()

    def reset_clock(self):
        timer.start_time = 0
        timer.time = 0
        timer.paused_time = 0

    def get_time(self):
        timer.time += timer.clock.get_time()
        return (timer.time / 1000) - timer.start_time