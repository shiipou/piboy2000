import pygame

import config as cfg
from window.window import Window

 
class Stat(Window):

    def __init__(self, screen, parent):
        super(Stat, self).__init__(screen, parent)
        self._running = False

    def on_init(self):
        super(Stat, self).on_init()
        self._running = True
        return True
    
    def on_event(self, event):
        super(Stat, self).on_event(event)

    def on_loop(self):
        super(Stat, self).on_loop()
    def on_render(self):
        super(Stat, self).on_render()
    def on_exit(self):
        super(Stat, self).on_exit()
    def exit(self):
        super(Stat, self).exit()
