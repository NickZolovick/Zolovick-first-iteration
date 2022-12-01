import sys
import pygame
from pygame.locals import *
from movingblock import Moving_Block
from background_block import Backgroundblock
from ball import Ball
from Finalsettings import Settings


class Brickbreaker:
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

        # Background block settings
        self.background_block_height = 15
        self.background_block_width = 45

        pygame.init()
        self.settings = Settings

        self.screen = pygame.display.set_mode((900, 600))  # pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Nick's Bricks")

        self.movingblock = Moving_Block(self)
        self.ball = Ball(self)
        self.backgroundblock = Backgroundblock(self)

    def run_game(self):
        self._check_events()
        self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        # to move the ship left and right
        if event.key == pygame.K_RIGHT:
            self.movingblock.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.movingblock.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.movingblock.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.movingblock.moving_left = False

    def _create_fleet(self):
        """Create the fleet of blocks."""
        # Make a block and find the number of blocks in a row
        # Spacing between each block is equal to one block width.
        backgroundblock = Backgroundblock(self)
        background_block_width, background_block_height = backgroundblock.rect.size
        available_space_x = self.settings.screen_width - (2 * background_block_width)
        number_aliens_x = available_space_x // (2 * background_block_width)

        # Determine the number of rows of blocks that fit on the screen.
        ball_height = 2 * self.ball.radius
        available_space_y = (self.settings.screen_height - (3 * background_block_height) - ball_height)
        number_rows = available_space_y // (2 * background_block_height)

        # Create the full fleet of blocks
        for row_number in range(number_rows):
            for background_block_number in range(number_aliens_x):
                self._create_background_block(background_block_number, row_number)

    def _create_background_block(self, alien_number, row_number):
        """Create a block and place it in the row."""
        background_block = background_block(self)
        background_block_width, background_block_height = background_block.rect.size
        background_block.x = background_block_width + 2 * background_block_width * background_block_number
        background_block.rect.x = background_block.x
        background_block.rect.y = background_block_height + 2 * background_block.rect.height * row_number
        self.backgroundblock.add(background_block)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = Brickbreaker()
    ai.run_game()
