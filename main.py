import pygame

import os
import signal
import subprocess

import config as cfg
from utils.window import Window

from window.stat import Stat

class Piboy2000:
 
    def __init__(self):
        
        # Trap exit signal
        signal.signal(signal.SIGINT, self.exit)
        signal.signal(signal.SIGTERM, self.exit)

        # Initialize pygame for video ouput
        pygame.init()
        #Set title on the window (Visible only if app is running from Desktop, not from CLI)
        pygame.display.set_caption("Piboy2000")

        # Properties :
        ## window is the current view objet
        self.window = None
        ## define default the height and width of the window
        self.WIDTH = cfg.screen_size_x
        self.HEIGHT = cfg.screen_size_y

        params = pygame.HWSURFACE | pygame.DOUBLEBUF
        if cfg.screen_fullscreen:
            params |= pygame.FULLSCREEN # add fullscreen flag
            try:
                # Get the computer screen size
                screen_info = pygame.display.Info()
                # replace the height and width of the window to became fullscreen
                self.WIDTH, self.HEIGHT = screen_info.current_w, screen_info.current_h
            except:
                pass
        self.screen = pygame.display.set_mode(self.get_size(), params)
        # Clock is to select a number of FPS
        self.clock = pygame.time.Clock()
        self.running = False

        # Show text
        ignore, font_size = Window.size((self.WIDTH, self.HEIGHT), (1, 24))
        font = pygame.font.Font(None, round(font_size))
        color = pygame.Color('forestgreen')
        self.text = font.render("testing scanlines", 1, color)
        self.text2 = font.render("line two", 1, color)

        # Create scanlines object for great video effect
        self.create_scanline()

        self.lines_position = list(range(0, self.HEIGHT + 1, 200))
        self.scanline_speed = 10

        # Start the loading video
        if cfg.load_skip_intro == False:
            subprocess.call(["omxplayer", "{}/videos/{}".format(cfg.file_resources_folder, 'boot_sequence.mp4')])
        self.window = Stat(self.screen, self)
 
    def create_scanline(self):
        self.scanline = pygame.Surface((1, 200))
        self.scanline = self.scanline.convert_alpha()
        color = pygame.Color(0, 200, 0)
        color.a = 15
        for a in range(100):
            color.g -= 1
            self.scanline.set_at((0, a), color)
            self.scanline.set_at((0, 199 - a), color)
 
        self.scanline = pygame.transform.scale(self.scanline, (self.WIDTH, 200))
 
    def draw(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.text, (80, 100))
        self.screen.blit(self.text2, (80, 150))
 
        ticks = pygame.time.get_ticks()
        for i in range(len(self.lines_position)):
            self.lines_position[i] -= self.scanline_speed
            if self.lines_position[i] < -199:
                self.lines_position[i] = self.HEIGHT
 
        for line in self.lines_position:
            self.screen.blit(self.scanline, (0, line), None, pygame.BLEND_RGBA_MULT)
            self.screen.blit(self.scanline, (0, line), None)
 
    def get_size(self):
        return self.WIDTH, self.HEIGHT
 
    def get_rect(self):
        return pygame.Rect(0,0,self.WIDTH,self.HEIGHT)
    
    def exit(self):
        self.running = False

    def loop(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.exit()
                    elif event.key == pygame.K_0:
                        if self.current_view != event.key:
                            self.window.exit()
                            self.current_view = event.key
                            self.window = Stat(self.screen, self)
            self.draw()
            pygame.display.flip()
            self.clock.tick(cfg.screen_fps)
 
        pygame.quit()
    
    def start(self):
        self.loop()

if __name__ == "__main__" :
    piboy2000 = Piboy2000()
    piboy2000.start()