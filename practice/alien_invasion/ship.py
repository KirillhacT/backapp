import pygame
from bullet import Bullet


class Ship:
    def __init__(self, screen, ai_settings):
        # Наш экран
        self.screen = screen
        self.image = pygame.image.load("images/pngwing.com.png")

        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.ai_settings = ai_settings

        #координата корабля в вещ типе
        self.center = float(self.image_rect.centerx)

    def blitme(self):
        """функция изображения корабля на экране"""
        self.screen.blit(self.image, self.image_rect)

    def update(self):
        """Функция обновления позиции корабля"""
        if self.moving_right and self.image_rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.image_rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.image_rect.centerx = self.center

    def fire_bullet(self, bullets):
        """Корабль стреляет"""
        if len(bullets) < self.ai_settings.bullet_allowed:
            new_bullet = Bullet(self.ai_settings, self.screen, self.image_rect)
            bullets.add(new_bullet)

