import pygame


class Backgroundblock:
    """A class to represent a single block in the sky"""

    def __init__(self, ai_game):
        """Initialize the block and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the block image and set its rect attribute.
        self.image = pygame.image.load('images/grayblock.png')
        self.rect = self.image.get_rect()

        # Start each new block near the top left corner of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the block's exact  horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if block is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
