import pygame
import sys
from bullet import Bullet
from mobs import Inos
import time

def events(screen, gun, bullets): #обработка событий
    for event in pygame.event.get():

        if event.type == pygame.QUIT: #если выйти
            sys.exit()

        elif event.type == pygame.KEYDOWN: #если кнопка нажата
            if event.key == pygame.K_d:#кнопка вправо
                gun.mright = True
            elif event.key == pygame.K_a:#кнопка влево
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP: #если кнопка отжата
            if event.key == pygame.K_d:# кнопка вправо
                gun.mright = False
            elif event.key == pygame.K_a:  # кнопка влево
                gun.mleft = False

def update (bg_color, screen, stats, sc, gun, mobss, bullets): #обновление экрана
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    mobss.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, sc, mobsarmy, bullets): #обновление позиций пуль
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, mobsarmy, True, True)
    if collisions:
        for mobsarmy in collisions.values():
            stats.score += 10 * len(mobsarmy)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()
    if len(mobsarmy) == 0:
        bullets.empty()
        create_army(screen, mobsarmy)

def gun_kill(stats, screen, sc, gun, mobsarmy, bullets): #столкновении пушки и армии
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        mobsarmy.empty()
        bullets.empty()
        create_army(screen, mobsarmy)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()

def update_mobs(stats, screen, sc, gun, mobsarmy, bullets): #обновляет позицию мобов
    mobsarmy.update()
    if pygame.sprite.spritecollideany(gun, mobsarmy):
        gun_kill(stats, screen, sc, gun, mobsarmy, bullets)
    mobs_check(stats, screen, sc, gun, mobsarmy, bullets)

def mobs_check(stats, screen, sc, gun, mobsarmy, bullets): #проверка добралась ли армия до конца экрана
    screen_rect = screen.get_rect()
    for mobs in mobsarmy.sprites():
        if mobs.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, mobsarmy, bullets)
            break

def create_army(screen, mobsarmy): #создание армии мобов
    mobs = Inos(screen)
    mobs_width = mobs.rect.width
    numbers_ino_x = int((700 - 2 * mobs_width) / mobs_width)
    mobs_height = mobs.rect.height
    numbers_ino_y = int((800 - 200 - 2 * mobs_height) / mobs_height)


    for row_number in range(numbers_ino_y - 6):
        for mobs_number in range(numbers_ino_x):
            mobs = Inos(screen)
            mobs.x = mobs_width + mobs_width * mobs_number
            mobs.y = mobs_height + mobs_height * row_number
            mobs.rect.x = mobs.x
            mobs.rect.y = mobs.rect.height + mobs.rect.height * row_number
            mobsarmy.add(mobs)

def check_high_score(stats, sc): #проверка новых рекордов
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))



