import sys
import pygame

from Finalsettings import settings
from movingblock import Moving_Block
from background_block import Backgroundblock
from ball import Ball


class Brickbreaker:
    """overall class to manage game assets and behavior"""

    def __init__(self):
        pygame.init()
        self.settings = settings

        self.screen = pygame.display.set_mode((900, 600))  # pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Nick's Bricks")

        self.movingblock = Moving_Block(self)
        self.ball = Ball(self)
        self.backgroundblock = Backgroundblock(self)

    def run_game(self):
        self._check_events()
        # self._update_screen()

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

    # def _check_ball_block_collisions(self):
    #     """Respond to ball_block collisions"""
    #     # Remove any blocks that the ball has hit
    #     # check to see if the ball hit a block, if so, get rid of the block.
    #     collisions = pygame.sprite.groupcollide(self.ball, self.background_block, True, True)
    #
    # def _update_screen(self):
    #     """Update images on the screen, and flip to the new screen."""
    #     self.screen.fill(self.Finalsettings.bg_color)
    #     self.block.blitme()
    #     for ball in self.ball.sprites():
    #         ball.draw_bullet()
    #     self.block.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = Brickbreaker()
    ai.run_game()
