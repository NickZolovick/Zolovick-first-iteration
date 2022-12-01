import pygame


class Moving_Block:
    """A class to manage the block."""

    def __init__(self, ai_game):
        """Initialize the block and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the block image and get its rect.
        self.image = pygame.image.load('images/grayblock.png')
        self.rect = self.image.get_rect()

        # Start each new block at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the block's horizontal position.
        self.x = float(self.rect.x)
        # Store a decimal value for the block's vertical position.
        self.y = float(self.rect.y)

        self.moving_block_pos = (self.x, self.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the block's position based on movement flags."""
        # Update the block's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.block_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.block_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the block at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_block(self):
        """Center the block on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
