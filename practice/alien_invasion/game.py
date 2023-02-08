import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    bg_color = ai_settings.bg_color
    ship = Ship(screen, ai_settings)
    # alien1 = Alien(ai_settings, screen, alien_path="alien.png")

    #Создание группы для хранения пуль
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, aliens, ship)
    while True:
        #Проверяем все евенты
        gf.check_events(ship, bullets)
        #Обновляем координаты корабля и пулек
        ship.update()
        bullets.update()
        #Удаляем пули, которые вышли за границы
        gf.update_bullets(bullets)
        #В конце концов обновляем экран
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)
    
if __name__ == "__main__":
    run_game()

