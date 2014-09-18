#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'


import pygame
import sys
import pygame.mixer
from pygame.locals import *

#pygame 初始化
pygame.init()

ScreenSize = (1024, 768)
clock = pygame.time.Clock()

#设置窗口模式及大小
screen = pygame.display.set_mode(ScreenSize)

pygame.mixer.set_num_channels(32)

#设置窗口标题
pygame.display.set_caption("抠图工具")

screenwidth = screen.get_width()
screenheight = screen.get_height()

explosions=0
