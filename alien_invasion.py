import sys

from settings import Settings

import pygame

class AlienInvasion:
    #Клас для управления ресурсами и поведением игры

    def __init__(self):
        #Инициализирует игру и создает игровые ресурсы
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #Назначение цвета фона
        self.bg_color = (230, 230, 230)

    def run_game(self):
        #Запуск игрового цикла игры
        while True:
            #Отслеживание событий клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #При каждом проходе цикла прорисовывается экран
            self.screen.fill(self.settings.bg_color)

            #Отображение последнего прорисованого эерана
            pygame.display.flip()

if __name__ == '__main__':
    #Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()

