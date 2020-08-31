import pygame.font

class Button():
    def __init__(self, ai_game, msg):
        '''Инициализирует атрибути кнопки'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #Назначение размеров и свойств кнопок
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #Построение обьекта rect кнопки и выражение по центру экрана
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #Сообщение кнопки создается только один раз
        self.prep_msg(msg)