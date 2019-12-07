import pygame
 
class Window:
    def __init__(self, screen):
        self.size = (0, 0)
        self.screen = screen
 
    def on_init(self):
        return True

    def on_event(self, event):
        pass
    
    def on_loop(self):
        pass
    def on_render(self):
        pass
    def on_exit(self):
        pass
    def exit(self):
        pass