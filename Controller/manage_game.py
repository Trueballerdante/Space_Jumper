import pygame
import sys
from View.main_menu import menu
from View.levels.level_one import level_1
from View.levels.level_two import level_2
from View.levels.level_three import level_3
from View.levels.level_four import level_4
from View.levels.level_five import level_5
from View.levels.level_six import level_6
from View.game_over_class import game_over
from View.add_time_view import add_time
from View.top_times_view import top_times
from View.levels.test_level import test_l
from Controller.timer_class import timer
from View.pause_view import pause_menu

class game_manager():
    def __init__(self, screen):
        self.screen = screen
        self.timer = timer()
        self.current_state = "main_menu"
        self.main_m = menu(self.screen)
        self.l1 = level_1(self.screen)
        self.l2 = level_2(self.screen)
        self.l3 = level_3(self.screen)
        self.l4 = level_4(self.screen)
        self.l5 = level_5(self.screen)
        self.l6 = level_6(self.screen)
        self.game_over = game_over(self.screen)
        self.top_times = top_times(self.screen)
        self.add_time = add_time(self.screen)
        self.test_l = test_l(self.screen)
        self.levels = {
            "level_one": self.l1,
            "level_two": self.l2,
            "level_three": self.l3,
            "level_four": self.l4,
            "level_five": self.l5,
            "level_six": self.l6
        }

        self.pause_menu = pause_menu(self.screen, self.levels)
        
    
    def manage_states(self):
        if(self.current_state == "main_menu"):
            self.timer.start_time = self.timer.clock.tick()
            self.current_state = self.main_m.run()
        if(self.current_state == "top_times"):
            self.current_state = self.top_times.run()
        if(self.current_state == "test_level"):
            self.current_state = self.test_l.run()
        if(self.current_state == "level_one"):
            self.timer.time += self.timer.clock.tick()
            timer.start_time = 0
            self.current_state = self.l1.run()
        if(self.current_state == "level_two"):
            self.timer.time += self.timer.clock.tick()
            self.current_state = self.l2.run()
        if(self.current_state == "level_three"):
            self.timer.time += self.timer.clock.tick()
            self.current_state = self.l3.run()
        if(self.current_state == "level_four"):
            self.timer.time += self.timer.clock.tick()
            self.current_state = self.l4.run()
        if(self.current_state == "level_five"):
            self.timer.time += self.timer.clock.tick()
            self.current_state = self.l5.run()
        if(self.current_state == "level_six"):
            self.timer.time += self.timer.clock.tick()
            self.current_state = self.l6.run()
        if(self.current_state == "game_over"):
            self.current_state = self.game_over.run()
            #self.timer.reset_clock() Dont delete. Needs further testing. The code was placed in game_over_class.py
            self.timer.start_time = self.timer.clock.tick()
        if(self.current_state == "add_time"):
            self.current_state = self.add_time.run()
        if(self.current_state == "pause_menu"):
            self.timer.start_time = self.timer.clock.tick()
            self.current_state = self.pause_menu.run()


