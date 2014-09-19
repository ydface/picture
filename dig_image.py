#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'


import pygame
import sys
import pygame.mixer
from pygame.locals import *
import mypygame


class DigImage(object):
    def __init__(self, father, key, image, x, y, w, h):
        super(DigImage, self).__init__()

        self.father = father
        self.key = key
        self.image = image
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.rect = Rect(self.x, self.y, self.w, self.h)
        self.clicked = False

    def get_ini(self):
        out = dict()
        out["key"] = self.key
        out["x"] = self.rect[0]
        out["y"] = self.rect[1]
        out["w"] = self.w
        out["h"] = self.h
        return  out
        #return '\"' + str(self.key) + '\":' + "{\"x\":" + str(self.rect[0]) + ",\"y\":" + str(self.rect[1]) + ",\"w\":" + str(self.w) + ",\"h\":" + str(self.h) + "}"

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            if self.rect.collidepoint(position):
                self.clicked = True
        if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
            position = pygame.mouse.get_pos()
            if self.rect.collidepoint(position):
                self.father.digs.remove(self)
        elif event.type == MOUSEMOTION:
            position = pygame.mouse.get_pos()
            if self.rect.collidepoint(position):
                rel = pygame.mouse.get_rel()
                if self.clicked:
                    self.rect[0] += rel[0]
                    self.rect[1] += rel[1]
        elif event.type == MOUSEBUTTONUP:
            if self.clicked:
                self.clicked = False
        elif event.type == KEYDOWN:
            if not self.clicked:
                return
            if event.key == K_LEFT:
                self.rect[0] -= 2
            elif event.key == K_RIGHT:
                self.rect[0] += 2
