import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Клас, представляющий одного пришельца'''

    def __init__(self, ai_game):
        '''Инициализирует пришельца и задает его начальную позицию'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Загрузка изображения пришельца и назначение атрибута rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Каждый новый пришелец появляется в левом углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Сохранение точной горизонтальной позиции пришельца
        self.x = float(self.rect.x)

    def update(self):
        '''Перемещает пришельца вправо'''
        self.x += self.settings.alien_speed
        self.rect.x = self.x