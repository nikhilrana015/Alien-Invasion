import pygame
from pygame.sprite import Group
from button import Button
from settings import Settings
from ShiP import Ship
from game_stats import GameStats
from scoreboard import Scoreboard
from pygame.sprite import Group
import Game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("ALIEN INVASION")
    #Make a play button
    play_button = Button(ai_settings,screen,"Play")
    #Create an instance to store game statistics
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    # Make a ship
    ship=Ship(ai_settings,screen)
    #Make a group to store bullets and aliens
    bullets = Group()
    aliens = Group()
    #Create a fleet of aliens
    gf.create_fleet(ai_settings,screen,ship,aliens)
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if(stats.game_active):
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
run_game()
