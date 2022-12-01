import sys
import pygame
from pygame.locals import *
from movingblock import Moving_Block
from background_block import Backgroundblock
from ball import Ball
from Finalsettings import settings


class Brickbreaker:
    # Overall class to manage game assets

    def __init__(self):
        pygame.init()

        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height),
                                              HWSURFACE | DOUBLEBUF | RESIZABLE)
        pic = pygame.image.load("images/space.png")
        self.screen.blit(pygame.transform.scale(pic, (self.screen_width, self.screen_height)), (0, 0))
        pygame.display.flip()

        # Moving block settings
        movingblock_width = 100
        movingblock_height = 20
        movingblock_speed = 1
        self.movingblock = Moving_Block(self)

        # Background block settings
        background_block_height = 20
        background_block_width = 100

        self.ball = Ball

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
        # to move the block left and right
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

    def check_ball_movingblock_collisions(self):
        """Respond to ball_moving block collisions"""
        # Bounce the ball back off the moving block
        if self.ball_pos == self.moving_block_pos:
            self.ball_speed = -1

    def _check_ball_background_block_collisions(self):
        """Respond to ball_background block collisions"""
        # Remove any block that has been hit by the ball, and bounce back the ball
        collisions = pygame.sprite.groupcollide(self.Ball, self.background_block, True, True)

    def create_background_block(self, background_block_number, row_number):
        """Initialize the block and set its starting position"""
        background_block = Backgroundblock(self)
        background_block_width, background_block_height = background_block.rect.size
        background_block.x = background_block_width + 2 * background_block_width * background_block_number
        background_block.rect.x = background_block.x
        background_block.rect.y = background_block_height + 2 * background_block.rect.height * row_number
        self.background_block.add(background_block)

    def _create_fleet(self):
        """Create the fleet of background blocks."""
        # Make an alien and find the number of aliens in a row
        # Spacing between each alien is equal to one Alien width.
        background_block = Backgroundblock(self)
        background_block_width, background_block_height = background_block.rect.size
        available_space_x = self.settings.screen_width - (2 * background_block_width)
        number_background_block_x = available_space_x // (2 * background_block_width)

        # Determine the number of rows of aliens that fit on the screen.
        movingblock_height = self.movingblock.rect.height
        available_space_y = (self.settings.screen_height - (3 * background_block_height) - movingblock_height)
        number_rows = available_space_y // (2 * background_block_height)

        # Create the full fleet of aliens
        for row_number in range(number_rows):
            for background_block_number in range(number_background_block_x):
                self.create_background_block(background_block_number, row_number)

    def _update_screen(self):
        self.movingblock.blitme()
        self.background_block.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = Brickbreaker()
    ai.run_game()
