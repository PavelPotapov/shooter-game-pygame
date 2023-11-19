import pygame
from vars import *
from random import randint


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed, sizes):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(img), sizes)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = sizes[0]
        self.height = sizes[1]

    def update(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Hero(GameSprite):
    def move(self):
        keys = pygame.key.get_pressed()
        if R_MODE_MOVE == 1:
            if keys[pygame.K_d] and self.rect.x < WIDTH - self.width - self.speed:
                self.rect.x += self.speed
            if keys[pygame.K_a] and self.rect.x > 0 + self.speed:
                self.rect.x -= self.speed
        if R_MODE_MOVE == 2:
            if keys[pygame.K_d]:
                self.rect.x += self.speed
            if keys[pygame.K_a]:
                self.rect.x -= self.speed
            if self.rect.x < -self.height // 2:
                self.rect.x = WIDTH - self.height // 2
            if self.rect.x > WIDTH - self.height // 2:
                self.rect.x = -self.height // 2


class Enemy(GameSprite):
    def move(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.x = randint(0, WIDTH - self.width)
            self.rect.y = -self.height
            self.speed = randint(1, 4)
            self.image = pygame.transform.scale(
                pygame.image.load(f"./img/{E_IMAGES[randint(0, 1)]}"), (self.width, self.height))
