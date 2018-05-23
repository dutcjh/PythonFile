# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 11:01:18 2018

@author: dutch
"""
import pygame,sys
from pygame.locals import *

pygame.init() #初始化pygame
screen=pygame.display.set_mode([1024,640])  #窗口大小：640*480
screen.fill([255,255,255])#用白色填充窗口
myimage=pygame.image.load('play.png') #把变量myimage赋给导入的图片
screen.blit(myimage,[100,400]) #在100,100的地方画出这个图片（100和100为左部和上部）
pygame.display.flip() 
play_flag = 0
ptime = 170.0
while True:
    for event in pygame.event.get():#获得事件
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN and 100<=event.pos[0]<=300 and \
         400<=event.pos[1]<=600: #判断鼠标位置以及是否摁了下去。
            #做需要做的事情，如开始游戏。
            if play_flag == 1:
                pygame.mixer.music.pause()
                ptime = ptime + pygame.mixer.music.get_pos()/1000.0
                print(ptime)
                play_flag = -1
            elif play_flag == 0:
                pygame.mixer.music.load("music.mp3")
                pygame.mixer.music.play()
                pygame.mixer.music.set_pos(ptime)
                play_flag = 1
            else:
                pygame.mixer.music.unpause()
                play_flag = 1
            

#pygame.init()
#pygame.mixer.init()
#screen=pygame.display.set_mode([512,512])
#background_image_filename = 'timg.jpg'
#background = pygame.image.load(background_image_filename).convert()
#pygame.time.delay(1000)
#pygame.mixer.music.load("music.mp3")
#pygame.mixer.music.play(0,120.0)
#while 1:
#    for event in pygame.event.get():
#        if event.type==pygame.QUIT:
#            sys.exit()
#    screen.blit(background, (0,0))
#    pygame.display.update()  
