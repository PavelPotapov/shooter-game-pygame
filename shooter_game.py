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
enemies_group = pygame.sprite.Group()


def create_enemies():
    for i in range(E_COUNTS):
        enemy = Enemy(f"./img/{E_IMAGES[randint(0, len(E_IMAGES) - 1)]}", randint(
            0, WIDTH - E_SIZE[0]), -E_SIZE[1], randint(1, 4), E_SIZE)
        enemies_group.add(enemy)
def check_click_cross():
    global GAME
    # перебор событий внешнего мира
    for e in pygame.event.get():
        if e.type == pygame.QUIT:  # крестик
            GAME = False

create_enemies()
while GAME:
    check_click_cross()
    window.blit(background_image, (0, 0))  # отобразили задний фон

    hero.draw(window)  # отобразили главного героя
    hero.move()

    enemies_group.draw(window)
    enemies_group.update()

    clock.tick(FPS)
    pygame.display.update()
