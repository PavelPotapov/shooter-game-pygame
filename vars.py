GAME = True  # Идет ли игра
FINISH = False  # Выиграли или проиграли ли мы
WIDTH = 1001  # Ширина окна
HEIGHT = 900  # Высота окна
FPS = 60
TITLE = "Shooter Game v0.1"  # Заголовок окна


# РАКЕТА
R_SIZE = (50, 70)
R_IMG = "rocket.png"
R_X = WIDTH // 2 - R_SIZE[0] // 2
R_Y = HEIGHT - R_SIZE[1]
R_SPEED = 5
# СПОСОБ ДВИЖЕНИЯ РАКЕТЫ. 1 - ударяемся в края, 2 - переносимся на противоположную сторону
R_MODE_MOVE = 2


# ВРАГИ
E_COUNTS = 10  # кол-во врагов
E_SIZE = (50, 50)
E_IMAGES = [f"enemies/ufo{i}.png" for i in range(1, 8)]

#ПУЛЯ
B_SIZE = (10, 20)
B_IMAGE = "bullet.png"
B_SPEED = 5

SHOOT_COUNT = 0 #кол-во подбитых врагов
COUNT_ENEMIES_TO_WIN = 30 #столько врагов нужно подбить, чтобы победить 
COUNT_ENEMIES_TO_LOSE = 30 #столько врагов нужно пропустить, чтобы проиграть 
HEALTHS = 5 #жизни
SHOOTS = 0 #сделанные выстрелы
TIME = 0 #Время игры

