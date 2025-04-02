import pygame
import datetime

pygame.init()

# Размер окна
size = width, height = 1400, 1050
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Clock")

# Загрузка изображений
clock_face = pygame.image.load("images/clock.png")
minute_hand = pygame.image.load("images/rightarm.png")
second_hand = pygame.image.load("images/leftarm.png")

# Масштабируем стрелки, если нужно
minute_hand = pygame.transform.scale(minute_hand, (50, 300))
second_hand = pygame.transform.scale(second_hand, (50, 300))

# Ограничение FPS
clock = pygame.time.Clock()

# Функция для отрисовки стрелок
def draw_hand(image, angle, pivot):
    rotated_image = pygame.transform.rotate(image, -angle)
    new_rect = rotated_image.get_rect(center=pivot)
    screen.blit(rotated_image, new_rect.topleft)

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_face, (0, 0))

    # Получаем текущее время
    now = datetime.datetime.now()
    minutes, seconds = now.minute, now.second

    # Вычисляем углы
    minute_angle = minutes * 6 + (seconds / 60) * 6
    second_angle = seconds * 6

    # Центр вращения стрелок
    pivot = (width // 2, height // 2 + 50)

    # Рисуем стрелки
    draw_hand(minute_hand, minute_angle, pivot)
    draw_hand(second_hand, second_angle, pivot)

    pygame.display.flip()

    # Обновляем экран раз в секунду
    clock.tick(1)

    # Обработка выхода
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()



   

