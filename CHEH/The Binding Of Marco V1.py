import pygame
from personnage import Personnage
from display import Display
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)

continuer= True

hero = Personnage()

degatsclic=1

#vpy=0

# INIT SALLE :
display = Display(fenetre)

#draw personnage

display.drawHero(hero)

pygame.display.flip()

# TODO: listprojectile = []

# boucle principale
while continuer:

    for event in pygame.event.get():
        keys = pygame.key.get_pressed()

        # GESTION MOUVEMENTS
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_w]:
                hero.haut = True
            if keys[pygame.K_s]:
                hero.bas = True
            if keys[pygame.K_a]:
                hero.gauche = True
            if keys[pygame.K_d]:
                hero.droite = True

            if keys[pygame.K_RIGHT]:
                if not projectile:
                    projectile_start_x = personnage_x
                    projectile_start_y = personnage_y
                    projectile = True
            if keys[pygame.K_LEFT]:
                if not projectile2:
                    projectile_start_x2 = personnage_x
                    projectile_start_y2 = personnage_y
                    projectile2 = True
            if keys[pygame.K_UP]:
                if not projectile3:
                    projectile_start_x3 = personnage_x
                    projectile_start_y3 = personnage_y
                    projectile3 = True
            if keys[pygame.K_DOWN]:
                if not projectile4:
                    projectile_start_x4 = personnage_x
                    projectile_start_y4 = personnage_y
                    projectile4 = True


        if event.type == pygame.KEYUP:
            if not keys[pygame.K_w]:
                hero.haut = False
            if not keys[pygame.K_s]:
                hero.bas = False
            if not keys[pygame.K_a]:
                hero.gauche = False
            if not keys[pygame.K_d]:
                hero.droite = False

        #LES DEGATS
        if event.type == KEYDOWN and event.key == K_q:

            if keys[pygame.K_q]:
                hero.vie -= degatsclic


        #GESTION QUITTER
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer = False

        # LES COLLISIONS PERSONNAGE


    hero.move()

    display.updateDisplay()

pygame.quit()
