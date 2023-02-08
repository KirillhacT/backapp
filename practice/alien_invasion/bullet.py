import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship_rect):
        super().__init__()
        self.screen = screen

        #Создание объекта пули (в виде прямоугольника)
        self.bullet_rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)

        #Задаем координаты по умолчанию (исходя из координат корабля)
        self.bullet_rect.centerx = ship_rect.centerx
        self.bullet_rect.top = ship_rect.top

        #Координата по y
        self.y = float(self.bullet_rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        #пуля все равно летит вверх
        self.y -= self.speed_factor
        self.bullet_rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.bullet_rect)

