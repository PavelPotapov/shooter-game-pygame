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
