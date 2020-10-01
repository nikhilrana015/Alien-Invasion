# Class for Settings

class Settings():
    def __init__(self):
        
        # Screen Settings
        self.screen_width=1000
        self.screen_height=720
        self.bg_color = (180,200,230)
        
        #Ship Settings
        self.ship_speed_factor = 2.0
        self.ship_limit = 3.0
        
        # bullet Settings
        self.bullet_speed_factor = 3.5
        self.bullet_width = 3.0
        self.bullet_height = 20
        self.bullet_color = 60,60,60
        self.bullets_allowed = 5
        
        # Alien settings
        self.alien_speed_factor = 3
        self.fleet_drop_speed = 11
        # fleet_direction of 1 represents right; -1 reprsents left
        self.fleet_direction = 2
        
        # How quickly the game speeds up
        self.speedup_scale = 1.6
        # How quickly alien point values increase
        self.score_scale = 2.0
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.8
        self.bullet_speed_factor = 4
        self.alien_speed_factor = 3
        self.fleet_direction = 2
        self.alien_points = 100

    def increase_speed(self):
        #Increase speed settings and alien point values
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        
