import pygame


class Ship():
    # Клас управления кораблем
    def __init__(self, ai_game):
        # Инициализирует корабыль и задает его начальную позицию
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Каждый новыий корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        #флаг перемещения
        self.moving_right = False

    def update(self):
        #Обновляет позицию корабля с учетом флага
        if self.moving_right:
            self.rect.x +=1

    def blitme(self):
        # Рисует корабль в текущей позиции
        self.screen.blit(self.image, self.rect)
