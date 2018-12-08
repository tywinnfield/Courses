#!/usr/bin/python3
# -*- coding: Utf-8 -*

#importation des bibliotheques


import pygame
from pygame.locals import *

from constantes_mg import *

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
#Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption(titre_fenetre)

    
#Chargement et affichage de l'écran d'accueil
fond = pygame.image.load(image_fond).convert()
fenetre.blit(fond, (0,0))


#Chargement et collage du personnage

perso = pygame.image.load("ressource/Gardien.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

gardien = pygame.image.load("ressource/Gardien.png").convert_alpha()
fenetre.blit(gardien, (10,10))

#rafraichissement de l'ecran
pygame.display.flip()

#Paramtre deplacement touche enfoncée
pygame.key.set_repeat(400, 30)
  
continuer = 1
#Boucle infinie
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
    
        if event.type == KEYDOWN:

            if event.key == K_DOWN:
                position_perso = position_perso.move(0,3)
           
            if event.key == K_UP:
                position_perso = position_perso.move(0,-3)
                
            if event.key == K_RIGHT: 
                position_perso = position_perso.move(3,0)

            if event.key == K_LEFT:
                position_perso = position_perso.move(-3,0)
                
		    
    #Re-collage

    fenetre.blit(fond, (0,0))   
    fenetre.blit(perso, position_perso)
    
    #Rafraichissement

    pygame.display.flip()
