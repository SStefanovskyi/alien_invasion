class Settings():
    # Клас для хранения всех настроек игры Alien Invasion

    def __init__(self):
        # Инициализирует настройки игры
        # Параметры экрана
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        #настройки корабля
        self.ship_speed = 1.5

        #Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_collor = (60, 60, 60)
