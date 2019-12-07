import pygame

import config as cfg
from window.window import Window

 
class Stat(Window):

    def __init__(self, screen, parent):
        super(Window, self).__init__(screen, parent)
        self._running = True

    def on_init(self):
        super(Window, self).on_init()
        while self.__running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            self.clock.tick(cfg.screen_fps)
        self.on_exit()
        return True
    
    def on_event(self, event):
        super(Window, self).on_event(event)

    def on_loop(self):
        super(Window, self).on_loop()
    def on_render(self):
        super(Window, self).on_render()
    def on_exit(self):
        super(Window, self).on_exit()
    def exit(self):
        super(Window, self).exit()
