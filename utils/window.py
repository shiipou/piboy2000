import pygame

import config as cfg

class Ticker:
    def __init__(self, length):
        self.next_tick = length
        self.length = length
 
    def elapse(self, ticks):
        if ticks > self.next_tick:
            self.next_tick += self.length
            return True
        return False

class Window():
        
    def size(screen_size, point):
        size_x, size_y = screen_size
        pos_x, pos_y = point
        return (size_x/cfg.screen_size_x*pos_x, size_y/cfg.screen_size_y*pos_y)
        