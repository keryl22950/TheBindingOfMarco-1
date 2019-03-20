import pygame
from personnage import Personnage
from pygame.locals import *


class Display:

    def __init__(self, fenetre):

        self.fond = pygame.image.load("texturefond.jpg").convert_alpha()
        self.fond = pygame.transform.scale(self.fond, (2120, 1280))

        self.sallesol = pygame.image.load("sol1.jpg").convert_alpha()
        self.sallesol = pygame.transform.scale(self.sallesol, (1620, 880))

        self.fenetre = fenetre

        self.drawWall()

    def drawWall(self):

        self.fenetre.blit(self.fond, (-100,-100))
        self.fenetre.blit(self.sallesol,(150,100))

        self.murhaut = pygame.draw.rect(self.fenetre,(52, 51, 51),[150,100,1620,50])
        self.murdroit = pygame.draw.rect(self.fenetre,(52, 51, 51),[1770,100,50,880])
        self.murbas = pygame.draw.rect(self.fenetre,(52, 51, 51),[150,930,1620,50])
        self.murgauche = pygame.draw.rect(self.fenetre,(52, 51, 51),[150,100,50,880])

    def updateDisplay(self):

        self.fenetre.blit(self.sallesol,(150,100))

        self.murhaut = pygame.draw.rect(self.fenetre,(52, 51, 51),[150,100,1620,50])
        self.murdroit = pygame.draw.rect(self.fenetre,(52, 51, 51),[1770,100,50,880])
        self.murbas = pygame.draw.rect(self.fenetre,(52, 51, 51),[150,930,1620,50])
        self.murgauche = pygame.draw.rect(self.fenetre,(52, 51, 51),[150,100,50,880])

        self.fenetre.blit(self.hero.image, (self.hero.x,self.hero.y))
        pygame.display.flip()

    def drawHero(self, hero):

        self.fenetre.blit(hero.image, (hero.x,hero.y))
