import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_function as gf
from game_state import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings = Settings()#设置
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("外星人游戏")

    #创建一艘飞船
    ship = Ship(ai_settings, screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    #创建一个外星人编组
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    #创建play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建存储游戏分数的实例
    sb = Scoreboard(ai_settings, screen, stats)


    #设置背景色
    bg_color = (0, 255, 0)

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
 


run_game()