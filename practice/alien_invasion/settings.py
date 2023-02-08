from typing import Tuple
class Settings:
    def __init__(self):
        self.ship_speed_factor: float = 1.2
        self.screen_width: int = 1400
        self.screen_height: int = 800
        self.bg_color: Tuple[int, int, int] = (255, 255, 255)

        #Параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

