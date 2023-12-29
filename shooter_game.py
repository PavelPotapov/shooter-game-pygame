# Создай собственный Шутер!
import pygame
from vars import *
import music
from base import *
from time import time


pygame.init()

# Окно игровое
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
pygame.display.set_icon(pygame.image.load("./img/rocket.png"))
background_image = pygame.transform.scale(
    pygame.image.load("./img/galaxy.jpg"), (WIDTH, HEIGHT))

# игровой таймер
clock = pygame.time.Clock()

# работа со шрифтами
text_shoot_count = TextHelper(x=10, y=10, size=25, color_text=(
    139, 240, 119), text=f"Подбито врагов: {SHOOT_COUNT}", font="./fonts/customFont1.ttf")
text_shoots = TextHelper(x=10, y=10 + 45 * 1, size=25, color_text=(
    127, 156, 240), text=f"Выстрелы: {SHOOTS}", font="./fonts/customFont1.ttf")
text_health = TextHelper(x=10, y=10 + 45 * 2, size=25, color_text=(
    237, 82, 57), text=f"Жизни: {SHOOTS}", font="./fonts/customFont1.ttf")
text_lose_enemies = TextHelper(x=10, y=10 + 45 * 3, size=25, color_text=(
    250, 163, 37), text=f"Пропущено врагов: {EnemiesInfo.LOSE_ENEMIES}", font="./fonts/customFont1.ttf")
text_time = TextHelper(x=10, y=10 + 45 * 4, size=25, color_text=(
    255, 255, 255), text=f"Время игры: {TIME}", font="./fonts/customFont1.ttf")
text_win = TextHelper(x=WIDTH // 2 - 130, y=HEIGHT // 2 - 50 // 2, size=50, color_text=(
    0, 255, 0), text="ТЫ ПОБЕДИЛ", font="./fonts/customFont1.ttf")
text_lose = TextHelper(x=WIDTH // 2 - 130, y=HEIGHT // 2 - 50 // 2, size=50, color_text=(
    255, 0, 0), text="ТЫ ПРОИГРАЛ", font="./fonts/customFont1.ttf")
text_restart = TextHelper(x=WIDTH // 2 - 185, y=HEIGHT // 2 + 50, size=25, color_text=(
    255, 255, 255), text="Нажми R чтобы начать заново", font="./fonts/customFont1.ttf")


hero = Hero(f"./img/{R_IMG}", R_X, R_Y, R_SPEED, R_SIZE)
enemies_group = pygame.sprite.Group()
bullets_group = pygame.sprite.Group()
animations = []


def create_enemy():
    enemy = Enemy(f"./img/{E_IMAGES[randint(0, len(E_IMAGES) - 1)]}",
                  randint(0, WIDTH - E_SIZE[0]), -E_SIZE[1], randint(1, 4), E_SIZE)
    enemies_group.add(enemy)

def create_enemies():
    for i in range(E_COUNTS):
        create_enemy()

def check_events():
    global GAME, SHOOTS
    # перебор событий внешнего мира
    for e in pygame.event.get():
        if e.type == pygame.QUIT:  # крестик
            GAME = False
        if e.type == pygame.KEYDOWN:  # нажата ли клавиша
            if e.key == pygame.K_SPACE:  # пробел ли
                if (not FINISH):
                    bullet = hero.shoot()
                    SHOOTS += 1
                    bullets_group.add(bullet)
                    music.fire_sound.play()

            if e.key == pygame.K_r:
                if (FINISH):
                    restart()

def update_texts():
    text_shoot_count.rerender(f"Подбито врагов: {SHOOT_COUNT}")
    text_shoots.rerender(f"Выстрелы: {SHOOTS}")
    text_health.rerender(f"Жизни: {HEALTHS}")
    text_lose_enemies.rerender(f"Пропущено врагов: {EnemiesInfo.LOSE_ENEMIES}")
    text_time.rerender(f"Время игры: {TIME}")

def draw_texts():
    text_shoot_count.draw(window)
    text_shoots.draw(window)
    text_health.draw(window)
    text_lose_enemies.draw(window)
    text_time.draw(window)

def check_collide_bullets():
    global SHOOT_COUNT
    # проверяем столкновения группы врагов с группой пулек, значения True и True означают, что и враг и пулька должны уничтожиться
    collisions = pygame.sprite.groupcollide(
        enemies_group, bullets_group, True, True)

    for enemy, bullet in collisions.items():
        SHOOT_COUNT += 1
        animation = Animation("img/animation_images",
                              enemy.rect.x, enemy.rect.y, (75, 75), ratio=8)
        animations.append(animation)
        create_enemy()  # создаем нового врага, потому что одного уже уничтожили, должен быть баланс врагов во вселенной


def check_collide_hero():
    global HEALTHS
    collisions = pygame.sprite.spritecollide(hero, enemies_group, True)
    for enemy in collisions:
        HEALTHS -= 1
        create_enemy()  # создаем нового врага, потому что одного уже уничтожили, должен быть баланс врагов во вселенной

def check_win():
    global SHOOT_COUNT, COUNT_ENEMIES_TO_WIN, FINISH
    if SHOOT_COUNT >= COUNT_ENEMIES_TO_WIN:
        text_win.draw(window)
        text_restart.draw(window)
        FINISH = True

def check_lose():
    global COUNT_ENEMIES_TO_LOSE, FINISH, HEALTHS
    if EnemiesInfo.LOSE_ENEMIES >= COUNT_ENEMIES_TO_LOSE or HEALTHS <= 0:
        text_lose.draw(window)
        text_restart.draw(window)
        FINISH = True

def restart():
    global SHOOT_COUNT,  COUNT_ENEMIES_TO_WIN, COUNT_ENEMIES_TO_LOSE, HEALTHS, SHOOTS, TIME, start_time, FINISH
    SHOOT_COUNT = 0  # кол-во подбитых врагов
    COUNT_ENEMIES_TO_WIN = 30  # столько врагов нужно подбить, чтобы победить
    COUNT_ENEMIES_TO_LOSE = 5  # столько врагов нужно подбить, чтобы победить
    EnemiesInfo.LOSE_ENEMIES = 0
    HEALTHS = 5  # жизни
    SHOOTS = 0  # сделанные выстрелы
    TIME = 0  # Время игры
    start_time = time()
    enemies_group.empty()
    bullets_group.empty()
    create_enemies()
    hero.rect.x = R_X
    hero.rect.y = R_Y
    FINISH = False

def check_animation():
    for animation in animations:
        animation.draw(window)
        animation.show_animation()
        if (animation.isKilled):
            animations.remove(animation)


create_enemies()
start_time = time()
while GAME:
    check_events()
    if (not FINISH):
        window.blit(background_image, (0, 0))  # отобразили задний фон

        check_animation()

        hero.draw(window)  # отобразили главного героя
        hero.move()

        enemies_group.draw(window)
        enemies_group.update()

        bullets_group.draw(window)
        bullets_group.update()

        check_collide_bullets()  # проверка на столкновение с пульками
        check_collide_hero()  # проверка на столкновение с героем

        check_win()
        check_lose()

        clock.tick(FPS)
        end_time = time()
        TIME = str(int(end_time - start_time)) + " сек."
    update_texts()
    draw_texts()
    pygame.display.update()
