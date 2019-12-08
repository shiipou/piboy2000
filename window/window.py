import pygame
 
class Window:
    def __init__(self, screen, parent):
        self.parent = parent
        self._running = False
        self.size = parent.get_size()
        self.screen = screen
        self.background = None
        self.on_init()
 
    def on_init(self):
        self._running = True
        return True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.on_exit()
    
    def on_loop(self):
        if self.background:
            background = pygame.image.load(self.background)
            screen.blit(background, self.size)

    def on_render(self):
        pygame.display.flip()

    def on_exit(self):
        self._running = False
    def exit(self):
        self.on_exit()