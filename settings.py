class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.ship_limit = 3
        # Maximum amount of lives is 3!
        if self.ship_limit > 3:
            raise Exception("Maximum amount of ships reached")

        # Bullet settings
        self.bullet_speed = 2
        self.bullet_width = 8
        self.bullet_height = 17
        self.bullet_color = (255, 255, 255)
        if self.bullet_color != (255, 255, 255):
            raise Exception("Wrong Bullet color used!")
        self.bullets_allowed = 10
        if self.bullets_allowed >= 11:
            raise Exception("Maximum amount of Bullets reached!")

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.3
        if self.speedup_scale >= 1.8:
            raise Exception("Speedup_Scale Too High")

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Settings that change throughout the game."""
        self.ship_speed = 4
        # Maximum ship starting speed is 5
        if self.ship_speed > 5:
            raise Exception("Starting Speed too High!")
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)