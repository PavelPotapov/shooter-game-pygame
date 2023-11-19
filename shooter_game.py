# Создай собственный Шутер!
import pygame
from vars import *
import music
from base import *


pygame.init()

# Окно игровое
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
pygame.display.set_icon(pygame.image.load("./img/rocket.png"))
background_image = pygame.transform.scale(
    pygame.image.load("./img/galaxy.jpg"), (WIDTH, HEIGHT))

# игровой таймер
clock = pygame.time.Clock()

hero = Hero(f"./img/{R_IMG}", R_X, R_Y, R_SPEED, R_SIZE)

enemy1 = Enemy(f"./img/{E_IMAGES[randint(0, 1)]}", 0, 0, 3, E_SIZE)


def check_click_cross():
    global GAME
    # перебор событий внешнего мира
    for e in pygame.event.get():
        if e.type == pygame.QUIT:  # крестик
            GAME = False


while GAME:
    check_click_cross()
    window.blit(background_image, (0, 0))  # отобразили задний фон

    hero.update(window)  # отобразили главного героя
    hero.move()

    enemy1.update(window)
    enemy1.move()

    clock.tick(FPS)
    pygame.display.update()
