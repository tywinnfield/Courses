Feuille de route trouvé sur un repo Github

Versions
0.0: Void
C'est le néant. Il n'y a rien à part quelques idées.
0.1: Création du dépot sur github
0.2: Rédaction du fichier README.md
0.5: Expérimentations avec Pygame
1.0: Synthèse des méthodes utiles de Pygame
1.1: Première brique
Affichage d'une image de briques.
1.2: Mur de briques
Affichage des briques ou espaces en parcourant une liste à 2 dimensions 15*15, appelé map.
1.3: Personnages
Affichage de Mac Gyver et du garde à une certaine position.
La position de Mac Gyver est définie dans son objet et la position du garde est définie dans la map.
1.4: Mac Gyver se déplace
Gére les évenements clavier, met à jour la position de Mac Gyver et rafraîchit l'affichage.
Pas de gestion des collisions avec les murs et si Mac Gyver sort de la map le programme plante.
1.5: Mac Gyver se cogne
Gestion des collisions avec les murs et les bords de la map.
1.6: Mac Gyver gagne
Lorsque Mac Gyver arrive à la position du gardien le programme affiche un message de victoire et se termine.
1.7: Refonte du programme
Le programme est découpé en modules et est mieux organisé
1.8: Environnement virtuel
Mise en place d'un environnement virtuel
1.9: Bêta de la 2.0
Test du programme, relecture du code et correction des bugs.
2.0: Animer le personnage (branche stable)
Version majeure du programme. Célébration avec une pizza !
2.1: Chargement de la map a partir d'un fichier
2.2: Détection de la position de Mac Gyver
2.3: Gestion de la position des objets et leur affichage
2.4: Gestion de la collecte des objets
2.5: Répartition aléatoire des objets
Algorithme basique, il y a un risque de "collision" avec la position d'un objet existant.
2.6: Mac Gyver perd
Lorsque Mac Gyver arrive à la position du gardien et n'a pas les 3 objets il perd et le programme se termine.
2.7: Docstrings
Documentation du code
2.8: DRY
Don't Repeat Yourself. Regroupement du code en methodes et autres structures.
2.9: Bêta de la 3.0
Test du programme, relecture du code et correction des bugs.
3.0: Récupérer les objets (branche stable)
3.1: Fichier config.json
Le fichier contient la configuration des variables suivants:
Message lors de la collecte d'un objet, message de début et fin de partie
Les noms des images a charger (+ images dans un dossier à part)
Le nom des objets
3.2: Programme plus fléxible
Nombre d'objets variable: pour ajouter un objet il suffit de modifier le fichier config.json et rien d'autre.
Taille de la map variable: pour modifier la taille de la map il suffit de modifier une constante et adapter le fichier map.xsb.
3.3: Affichage des messages/dialogues dans la console
3.4: Amélioration de l'algorithme de répartition des objets (éviter leur apparition sur une même case)
3.5: N'afficher que Mac Gyver ou le gardien lorsqu'ils se trouvent sur la même case (en fonction de la victoire ou perte)
3.6: Replay
Proposer de rejouer à la fin d'une partie.
La position des objets est réinitialisée, Mac Gyver replacé sur sa position initiale et son inventaire est vidé.
3.7: PEP8
Vérification du code avec Pylint
3.8: Gestion des erreurs
Ajout de messages d'erreur clairs pour les utilisateurs du programme:
Changement de noms des fichiers du programme (par ex. si l'utilisateur essaye de remplacer une image par une autre).
Modification du config.json et oubli de spécifier un message, ou lien vers l'image de l'objet incorrect.
Oubli de définir la position initiale du personnage dans le fichier map.xsb (les autres erreurs ne sont pas gérées !).
3.9: Bêta de la 4.0
Test du programme, relecture du code et correction des bugs.
4.0: Gagner ! (branche stable) <---- je suis ici !
4.9: Bêta de la 5.0
Test du programme, relecture du code et correction des bugs.
5.0: Intelligence artificielle (branche stable)

