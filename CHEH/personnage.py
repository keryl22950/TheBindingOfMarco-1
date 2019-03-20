import pygame
from pygame.locals import *

class Personnage:

    def __init__(self):

        self.gauche = False
        self.droite = False
        self.haut = False
        self.bas = False

        self.x = 800
        self.y = 625

        self.vie = 3

        self.pspeed = 3
        self.range = 700

        self.image = pygame.image.load("marco.jpg").convert_alpha()

    def coord(self):

        print("coordx : " + str(self.x) + " ; coordy : " + str(self.y))

    def move(self):

        if self.gauche:
            hero.x -= 1
        if self.droite:
            hero.x += 1
        if self.haut:
            hero.y -= 1
        if self.bas:
            hero.y += 1

        if self.y == 95 :
            hero.haut = False
        if self.y == 677 :
            hero.bas = False
        if self.x == 134 :
            hero.gauche = False
        if self.x == 1536 :
            hero.droite = False
