import pygame


class Ball:
    """A class to represent the ball flying around"""

    def __init__(self, ai_game):
        # Help from Matt McClelland on how to create a ball and its properties
        ball = pygame.image.load("images/ball.png")
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.ball_color
        self.ball_color = self.settings.ball_color
        self.ball_speed = 1

        # Create a bullet rect at (0, 0) and then set correct position.
        self.circ = pygame.circle(0, 0, self.settings.ball_radius, self.settings.ball_radius)
        self.circ.midtop = ai_game.ship.rect.midtop

        # Store the ball's position as a decimal value.
        self.y = float(self.circ.y)
        self.x = float(self.circ.x)
        self.ball_pos = (self.x, self.y)

    def update(self):
        """Move the ball up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.ball_speed
        # Update the rect position.
        self.circ.y = self.y

    def draw_ball(self):
        """Draw the ball to the screen."""
        ball = pygame.image.load("images/ball.png")