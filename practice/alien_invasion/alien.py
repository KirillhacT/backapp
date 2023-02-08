import pygame.image

from settings import Settings
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self, ai_settings: Settings, screen, alien_path="alien.png"):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load(f"images/{alien_path}")
        self.alien_rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.alien_rect.x = self.alien_rect.width
        self.alien_rect.y = self.alien_rect.height

        # Сохранение точной позиции пришельца.
        self.position_x = float(self.alien_rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.alien_rect)




