import pygame
import sys
from pygame.locals import *

pygame.init()

size = width,height=600,400

speed=[-2,1]
bg=(255,255,255)

#创建指定大小的窗口 Surface

screen = pygame.display.set_mode(size)

# 设置窗口标题
pygame.display.set_caption("初次见面，请大家多多关照！")

#加载图片
turtle = pygame.image.load( 'G:\\Grandy\\Python\\lianxi\\Function\GAME\\xiaogui\\turtle.png')

#获取图片位置
position=turtle.get_rect()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    #移动图像
    position = position.move(speed)

    if position.left<0 or position.right>width:
        #移动图像
        turtle = pygame.transform.flip(turtle,True,False)
        #反向移动
        speed[0]=-speed[0]

    if position.top<0 or position.bottom>height:
        speed[1]=-speed[1]

    # 填充背景
    screen.fill(bg)
    # 更新图像
    screen.blit(turtle,position)

    # 更新界面
    pygame.display.flip()
    #延迟10毫秒
    pygame.time.delay(10)
    #界10面