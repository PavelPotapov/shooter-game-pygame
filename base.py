import pygame
from vars import *
from random import randint
import vars
import os


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

    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Animation():
    def __init__(self, folder_name, x, y, sizes, ratio=5):
        self.images = os.listdir(folder_name)
        self.current_image = pygame.transform.scale(
            pygame.image.load(folder_name + "/" + self.images[0]), sizes)
        self.rect = self.current_image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sizes = sizes
        self.number_image = 0
        self.ratio = ratio
        self.folder_name = folder_name
        self.isKilled = False

    def show_animation(self):
        self.number_image += 1
        if self.number_image >= len(self.images) * self.ratio:
            self.isKilled = True
        else:
            self.current_image = pygame.transform.scale(
                pygame.image.load(self.folder_name + "/" + self.images[self.number_image // self.ratio]), self.sizes)

    def draw(self, win):
        win.blit(self.current_image, (self.rect.x, self.rect.y))


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

    def shoot(self):
        return Bullet(f"./img/{B_IMAGE}", self.rect.x + self.width // 2 - B_SIZE[0] // 2, self.rect.y, B_SPEED, B_SIZE)


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < -self.height:
            self.kill()


class EnemiesInfo:
    LOSE_ENEMIES = 0


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            EnemiesInfo.LOSE_ENEMIES += 1
            self.rect.x = randint(0, WIDTH - self.width)
            self.rect.y = -self.height
            self.speed = randint(1, 4)
            self.image = pygame.transform.scale(pygame.image.load(
                f"./img/{E_IMAGES[randint(0, len(E_IMAGES) - 1)]}"), (self.width, self.height))


class TextHelper():
    def __init__(self, x, y, size, color_text, text, font=None):
        self.font = pygame.font.Font(font, size)
        self.text = self.font.render(text, True, color_text)
        self.message = text
        self.x = x
        self.y = y
        self.color_text = color_text

    def rerender(self, new_text):
        self.text = self.font.render(new_text, True, self.color_text)

    def change_color(self, new_color):
        self.color_text = new_color
        self.rerender(self.message)

    def draw(self, window):
        window.blit(self.text, (self.x, self.y))
