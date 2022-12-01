from pygame.locals import *
import pygame
import time
pygame.init()


class settings:
    """A class to store all settings for FinalGame."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (30, 30, 30)

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height),
                                              HWSURFACE | DOUBLEBUF | RESIZABLE)
        pic = pygame.image.load("images/space.png")
        self.screen.blit(pygame.transform.scale(pic, (self.screen_width, self.screen_height)), (0, 0))
        pygame.display.flip()

        # block settings
        self.block_speed = 0.5

        # Ball settings
        self.ball_speed = 0.25
        self.ball_width = 15
        self.ball_height = 15
        self.ball_color = (150, 150, 150)
        self.ball_allowed = 3
        self.ball_radius = 8
        self.ball_radius = 15

        # Background block settings
        self.background_block_height = 15
        self.background_block_width = 45


pygame.init()
# define the screen size
screen_width = 700
screen_height = 500
# set the screen, upload, display the picture
screen = pygame.display.set_mode((screen_width, screen_height), HWSURFACE | DOUBLEBUF | RESIZABLE)
pic = pygame.image.load("images/space.png")
screen.blit(pygame.transform.scale(pic, (screen_width, screen_height)), (0, 0))
pygame.display.flip()
time.sleep(3)
