class Settings():
    # Клас для хранения всех настроек игры Alien Invasion

    def __init__(self):
        # Инициализирует настройки игры
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #настройки корабля
        self.ship_speed = 1.5

        #Настройки пришельцев
        self.alien_speed = 1.0

        #Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_collor = (60, 60, 60)
        self.bullets_allowed = 3