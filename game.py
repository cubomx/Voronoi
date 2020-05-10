import pygame, sys
from pygame.locals import *
from random import randint
from pygame import gfxdraw

def pygame_init():
    pygame.init()
    windowSurface = pygame.display.set_mode((500, 500), 0, 32)
    return windowSurface

def drawPoints(points, window):
    window.fill((255,255,255))
    for p in points:
        randColor = (randint(0, 255), randint(0, 255), randint(0, 255))
        randPoint = (randint(0, 255), randint(0, 255), randint(0, 255))
        for individual in p[2]:

            gfxdraw.pixel(window, p[0] + individual[0], p[1] +individual[1], randColor)
        pygame.draw.circle(window, randPoint,  (p[0], p[1]),  4, 1)

def stayForever():
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.display.flip()