import pygame
from pygame.locals import *

class Projectile:

    def __init__(self, x, y, dir, pers):

        self.x = x
        self.y = y
        self.dir = dir
        self.pers = pers

    def coord(self):

        print("coordx : " + str(self.x) + " ; coordy : " + str(self.y))

    def tir(self):
        if projectile:
            projectileDecalage += projectileSpeed
            pygame.draw.circle(fenetre, (225,255,255), (projectile_start_x + 170 + projectileDecalage, projectile_start_y + 135), 20)
            projectile_x= projectile_start_x + projectileDecalage
            if projectileDecalage > portee or projectile_x > 1580:
                projectileDecalage = 0
                projectile = False

        if projectile2:
            projectileDecalage2 -= projectileSpeed
            pygame.draw.circle(fenetre, (225,255,255), (projectile_start_x2 + 50 + projectileDecalage2, projectile_start_y2 + 135), 20)
            projectile_x2= projectile_start_x2 + projectileDecalage2
            if -projectileDecalage2 > portee or projectile_x2 < 170:
                projectileDecalage2 = 0
                projectile2 = False

        if projectile3:
            projectileDecalage3 -= projectileSpeed
            pygame.draw.circle(fenetre, (225,255,255), (projectile_start_x3 + 170 , projectile_start_y3 + 135 + projectileDecalage3), 20)
            projectile_y3= projectile_start_y3 + projectileDecalage3
            if -projectileDecalage3 > portee or projectile_y3 < 35:
                projectileDecalage3 = 0
                projectile3 = False

        if projectile4:
            projectileDecalage4 += projectileSpeed
            pygame.draw.circle(fenetre, (225,255,255), (projectile_start_x4 + 170 , projectile_start_y4 + 135 + projectileDecalage4), 20)
            projectile_y4= projectile_start_y4 + projectileDecalage4
            if projectileDecalage4 > portee or projectile_y4 > 772:
                projectileDecalage4 = 0
                projectile4 = False
