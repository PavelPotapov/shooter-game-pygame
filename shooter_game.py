# Создай собственный Шутер!
import pygame
from vars import *


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
pygame.display.set_icon(pygame.image.load("img/rocket.png"))

# игровой таймер
clock = pygame.time.Clock()


while GAME:
    # перебор событий внешнего мира
    for e in pygame.event.get():
        if e.type == pygame.QUIT:  # крестик
            GAME = False

    clock.tick(FPS)
    pygame.display.update()
