import pygame
import time
from plane_sprites import *

pygame.init()

# 游戏主窗口
window = pygame.display.set_mode((480, 700))
# 加载图片到内存
background = pygame.image.load("./images/background.png")
plane1 = pygame.image.load("./images/me1.png")
plane2 = pygame.image.load("./images/me2.png")
# 创建敌机精灵和精灵组
enemy_plane1 = GameSprite("./images/enemy1.png", speed=3)
enemy_plane2 = GameSprite("./images/enemy2.png", speed=2)
enemy_plane3 = GameSprite("./images/enemy3_n1.png")
enemy_group = pygame.sprite.Group(enemy_plane1, enemy_plane2, enemy_plane3)

# 设定一个时钟
clock = pygame.time.Clock()

# 创建飞机区域对象，设置初始位置189, 574，设置102, 126飞机大小
plane_obj = pygame.Rect(189, 574, 50, 50)

while True:

    # 游戏主窗口中显示背景图片
    window.blit(background, (0, 0))
    enemy_group.draw(window)
    enemy_group.update()
    # window.blit(plane2, (189, 574))
    # 刷新显示，必须要调用才能看到绘制的结果
    pygame.display.update()
    clock.tick(60)

    # # 游戏主窗口中显示背景图片
    # window.blit(background, (0, 0))
    # window.blit(plane1, plane_obj)
    # # 刷新显示，必须要调用才能看到绘制的结果
    # pygame.display.update()
    # plane_obj.y -= 1
    # clock.tick(5)

pygame.quit()