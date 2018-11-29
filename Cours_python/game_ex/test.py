#importation des bibliotheques

import pygame
from pygame.locals import *

#Inititalisation de la bibli Pygame
pygame.init()

#Creation de la fenêtre
fenetre = pygame.display.set_mode((640, 480),RESIZABLE)

#import de l'image de fond
fond = pygame.image.load("background.jpg").convert()

#superposition image de fond sur la surface de fond noire
fenetre.blit(fond, (0,0)) #1er para = image a coller, 2e = tuple de l'abscisse et ordonnee du point de collage

#chargement et collage du perso
perso = pygame.image.load("perso.png").convert_alpha()
perso_x = 0
perso_y = 0
fenetre.blit(perso, (perso_x, perso_y))


#rafraichissement de l'ecran
pygame.display.flip()


#activation touche enfoncée
pygame.key.set_repeat(400,30)

#Creation de la boucle si continue = 1, stoppe si = 0
continuer = 1
while continuer:
    for event in pygame.event.get(): #parcours la liste de tous les events
        if event.type == QUIT:# si on a un event QUITTER
            continuer = 0# on arrete la boucle
                
        if event.type == KEYDOWN:

            if event.key == K_DOWN: 
                perso_x = 0
                perso_y = 3
           
            if event.key == K_UP:
                perso_x = 0
                perso_y = -3

            if event.key == K_RIGHT: 
                perso_x = 3
                perso_y = 0

            if event.key == K_LEFT:
                perso_x = -3
                perso_y = 0

        if event.type == MOUSEBUTTONDOWN: 
            if event.button == 1:

                perso_x = event.pos[0]
                perso_y = event.pos[1]


    fenetre.blit(fond,(0,0))
    fenetre.blit(perso, (perso_x, perso_y))
    pygame.display.flip()





