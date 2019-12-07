import pygame

import signal

import config as cfg
from window.splash import Splash
from window.stat import Stat

class Piboy2000:

    def __init__(self):
        self._running = True
        self.size = (0, 0)
        self.screen = None
        self.window = None
        self.clock = pygame.time.Clock()

    def on_init(self):
        # Trap exit signal
        signal.signal(signal.SIGINT, self.on_exit)
        signal.signal(signal.SIGTERM, self.on_exit)
        
        pygame.init()

        screen_info = pygame.display.Info()

        self.size = self.weight, self.height = screen_info.current_w, screen_info.current_h
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN)
        
        self._running = True
        if Splash(self.screen, self).on_init():
            self.window = Stat(self.screen, self)
        else:
            self.on_exit()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.on_exit()
            elif event.key == pygame.K_0:
                if self.current_view != event.key:
                    self.current_view = event.key
                    self.window = Stat(self.screen, self)
        else:
            self.window.on_event(event)

    def on_loop(self):
        self.window.on_loop()
    def on_render(self):
        self.window.on_render()
    def on_exit(self):
        self._running = False
        pygame.quit()
    def start(self):
        self.on_execute()
    def exit(self):
        self.on_exit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            self.clock.tick(cfg.screen_fps)
        self.on_exit()

if __name__ == "__main__" :
    piboy2000 = Piboy2000()
    piboy2000.start()