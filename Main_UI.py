#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'


import pygame
import sys
import pygame.mixer
from pygame.locals import *
import mypygame

screen = mypygame.screen

swidth = mypygame.screenwidth
sheight = mypygame.screenheight

fwidth = swidth / 2

max_out = 512


class MainUI(object):
    TTF_Font = "resource/msyh.ttf"
    D_Font = pygame.font.Font(TTF_Font, 10)

    def __init__(self):
        super(MainUI, self).__init__()

        self.open_rect = Rect(fwidth + 10, 2, 60, 15)
        self.save_rect = Rect(fwidth + 240, 2, 60, 15)
        self.open_file = "resource/"
        self.input = False
        self.ratio = 1.0
        self.clicked = False
        self.s_x = 0
        self.s_y = 0
        self.t_x = 0
        self.t_y = 0
        self.in_image = None
        self.in_rect = Rect(0, 0, 0, 0)
        self.offest = 0

        self.out_image = pygame.surface.Surface((max_out, max_out), flags=SRCALPHA, depth=32)
        self.out_file = "resource/"
        self.output = False
        self.out_x = 0
        self.out_y = 0

        self.key_input = False
        self.key = ""
    def draw(self):
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 0), (fwidth, 0, 2, sheight))
        pygame.draw.rect(screen, (255, 255, 0), (fwidth, 20, fwidth, 2))

        pygame.draw.rect(screen, (255, 0, 0), self.open_rect)
        pygame.draw.rect(screen, (255, 0, 0), self.save_rect)
        MainUI.draw_label(u"打开", (self.open_rect[0] + 5, self.open_rect[1]))
        MainUI.draw_label(u"保存", (self.save_rect[0] + 5, self.save_rect[1]))
        MainUI.draw_label(self.open_file, (self.open_rect[0] + 60 + 5, self.open_rect[1]))
        MainUI.draw_label(self.out_file, (self.save_rect[0] + 60 + 5, self.save_rect[1]))

        if self.key_input:
            MainUI.draw_label(u"请输入key: " + self.key, (self.save_rect[0] + 185 + 5, self.save_rect[1]))

        screen.set_clip(fwidth, 20, fwidth, sheight)
        if self.in_image:
            screen.blit(self.in_image, self.in_rect)

        if self.s_x:
            pygame.draw.line(screen, (255, 255, 255), (self.s_x, self.s_y), (self.s_x, self.t_y))
            pygame.draw.line(screen, (255, 255, 255), (self.s_x, self.s_y), (self.t_x, self.s_y))
            pygame.draw.line(screen, (255, 255, 255), (self.t_x, self.s_y), (self.t_x, self.t_y))
            pygame.draw.line(screen, (255, 255, 255), (self.s_x, self.t_y), (self.t_x, self.t_y))

        screen.set_clip(0, 0, swidth, sheight)

        screen.blit(self.out_image, (0, 0))

    def handle_event(self,event):
        if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            if self.open_rect.collidepoint(position):
                self.input = True
            elif self.save_rect.collidepoint(position):
                self.output = True
            if position[0] > fwidth and position[1] > 20:
                self.clicked = True
                self.s_x = position[0]
                self.s_y = position[1]
        elif event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
            self.s_x = 0
            self.s_y = 0
            self.t_x = 0
            self.t_y = 0
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                self.in_rect[0] -= 5
                self.offest += 5
            elif event.key == K_RIGHT:
                self.in_rect[0] += 5
                self.offest -= 5
            elif self.input:
                if event.key == K_BACKSPACE:
                    self.open_file = self.open_file[:-1]
                elif event.key == K_RETURN:
                    self.in_image = MainUI.load_image(self.open_file)
                    self.in_rect = self.in_image.get_rect()
                    self.in_rect.topleft = (fwidth, 20)
                    self.open_file = "resource/"
                    self.input = False
                else:
                    self.open_file += event.unicode
            elif self.output:
                if event.key == K_BACKSPACE:
                    self.out_file = self.out_file[:-1]
                elif event.key == K_RETURN:
                    pygame.image.save(self.out_image, self.out_file)
                    self.out_file = "resource/"
                else:
                    self.out_file += event.unicode
            elif self.key_input:
                if event.key == K_BACKSPACE:
                    self.key = self.key[:-1]
                elif event.key == K_RETURN:
                    i_y = self.s_y - 20
                    i_x = self.s_x - fwidth + self.offest
                    w = self.t_x - self.s_x
                    h = self.t_y - self.s_y
                    image = self.in_image.subsurface((i_x, i_y), (w, h))
                    if self.out_x + w < max_out:
                        self.out_image.blit(image, (self.out_x, self.out_y))
                        print '\"' + self.key + '\":', "{\"x\":", self.out_x, ",\"y\":", self.out_y, ",\"w\":", w, ",\"h\":", h, "}"
                        self.out_x += w
                    else:
                        self.out_x = 0
                        self.out_y += h
                        self.out_image.blit(image, (self.out_x, self.out_y))
                        print '\"' + self.key + '\":', "{\"x\":", self.out_x, ",\"y\":", self.out_y, ",\"w\":", w, ",\"h\":", h, "}"
                    self.key = ""
                    self.key_input = False
                else:
                    self.key += event.unicode
        elif event.type == MOUSEMOTION:
            if self.clicked:
                position = pygame.mouse.get_pos()
                self.t_x = position[0]
                self.t_y = position[1]
        elif event.type == MOUSEBUTTONUP:
            if self.clicked:
                #if self.s_x:
                self.key_input = True
                self.output = False
                self.clicked = False


    @staticmethod
    def draw_label(text, pos):
        surface = MainUI.D_Font.render(text, True, (255, 255, 255))
        screen.blit(surface, pos)

    @staticmethod
    def load_image(path):
        try:
            image = pygame.image.load(path).convert_alpha()
        except pygame.error:
            print "can't load the image from", path
            raise SystemExit
        return image
