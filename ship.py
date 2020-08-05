import pygame


class Ship():
    # Клас управления кораблем
    def __init__(self, ai_game):
        # Инициализирует корабыль и задает его начальную позицию
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Каждый новыий корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        #Сохранение веществинной координаты центра корабля
        self.x = float(self.rect.x)

        #флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #Обновляется атрибут х, а не rect
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        #Обновление атрибута rect на основании self x
        self.rect.x = self.x

    def blitme(self):
        # Рисует корабль в текущей позиции
        self.screen.blit(self.image, self.rect)
