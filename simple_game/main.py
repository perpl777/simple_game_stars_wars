import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores

def run ():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption(('атака на Китсуню 1. Звездные войны'))
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    mobsarmy = Group()
    controls.create_army(screen, mobsarmy)
    stats = Stats()
    sc = Scores(screen, stats)

    while True: #пока игра открыта работают функции
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, mobsarmy, bullets)
            controls.update_bullets(screen, stats, sc, mobsarmy, bullets)
            controls.update_mobs(stats, screen, sc, gun, mobsarmy, bullets)
run()