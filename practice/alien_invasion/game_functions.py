import sys
import pygame
from alien import Alien
from settings import Settings

def check_keydown_events(event, ship, bullets):
    """Реагирует на нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.fire_bullet(bullets)

def check_keyup_events(event, ship):
    """Реагирует на отпускание клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship, bullets):
    """Проверка ивентов"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_bullets(bullets):
    """Удаление пуль на экране"""
    for bullet in bullets.copy():  # Перебираем все выпущенные пули
        if bullet.bullet_rect.bottom <= 0:  # Если она выбралась за границу экрана, то удаляем ее
            bullets.remove(bullet)


def update_screen(ai_settings: Settings, screen, ship, bullets, aliens):
    """Покадровое обновление экрана"""
    for bullet in bullets.sprites(): #Рисуем пули
        bullet.draw_bullet()
    pygame.display.flip()
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for alien in aliens:
        alien.blitme()

def get_number_aliens_x(ai_settings: Settings, alien_width) -> int:
    """Вычисляет количество пришельцев в ряду."""
    avalable_space_x = ai_settings.screen_width - alien_width // 2
    number_aliens_x = int(avalable_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings: Settings, ship_height, alien_height):
    """Определяет количество рядов, помещающихся на экране."""
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.alien_rect.width
    alien.position_x = alien_width + 2 * alien_width * alien_number
    alien.alien_rect.x = alien.position_x
    # alien.alien_rect.y = alien.alien_rect.height + 2 * alien.alien_rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings: Settings, screen, aliens, ship):
    """Создает флот пришельцев."""
    # Создание пришельца и вычисление количества пришельцев в ряду.
    # Интервал между соседними пришельцами равен одной ширине пришельца.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.alien_rect.width)
    number_rows = get_number_rows(ai_settings, ship.image_rect.height, alien.alien_rect.height)
    print(number_rows)
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)




