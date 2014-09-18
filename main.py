#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

#导入pygame模块，第8行的作用是简化你的输入，如不用在event前再加上pygame模块名
import pygame
from pygame.locals import *
import mypygame
import Main_UI

def hello_world():
    #循环，直到接收到窗口关闭事件
    ui = Main_UI.MainUI()
    running = True
    while running:
         #处理事件
        for event in pygame.event.get():
            #接收到窗口关闭事件
            if event.type == QUIT:
                running = False
            else:
                ui.handle_event(event)
        #将Surface对象绘制在屏幕上
        ui.draw()
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    hello_world()
