import pygame
 
class Window:
    def __init__(self, screen, parent):
        self.parent = parent
        self.size = parent.size
        self.screen = screen
        self.background = None
        self.on_init()
 
    def on_init(self):
        return True

    def on_event(self, event):
        pass
    
    def on_loop(self):
        if self.background:
            background = pygame.image.load(self.background)
            screen.blit(background, self.size)

    def on_render(self):
        pygame.display.flip()

    def on_exit(self):
        pass
    def exit(self):
        pass