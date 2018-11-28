from random import randrange
from math import ceil
#Demander au joueur de miser une somme sur un numéro entre 0 et 49

mise = input("Quelle somme souhaitez-vous parier ?")
mise = int(mise)

numero = input ("Sur quel numéro souhaitez-vous parier ?")
numero = int(numero)

value = randrange(50)
print(value)
    
if value == numero:
    mise = mise*3
    print("Vous avez le numéro exact ! Félicitation ! Vous remportez  $")
elif numero % 2 == value % 2:
    mise = ceil(mise * 0.5)
    print("Vous avez la bonne couleur ! Votre mise est de ")
else: print("Vous avez perdu")

