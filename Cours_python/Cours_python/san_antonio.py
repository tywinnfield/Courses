
# -*- coding: utf8 -*-

import random
import json


#fonction pour lire le fichier characters.json et le convertir en liste
def read_values_from_json(file, key):
    values = [] # Create a new empty list
    with open(file) as f:# Open a json file with my objects
        data = json.load(f) # load all the data it contains. data = entries
        for entry in data: # add each item in my list
            values.append(entry[key])
    return values  # return my completed list

def message(character, quote):
    n_character = character.capitalize()
    n_quote = quote.capitalize()
    return "{} a dit : {}".format(n_character, n_quote)

def get_random_item(my_list):
# show random quote
    rand_num = random.randint(0, len(my_list) -1)
    item = my_list[rand_num] # get a quote from list
    return(item) # return the item

# return a random value from a json file - formule générale
# def random_value():
    # all_values = read_values_from_json()
    # return get_random_item(all_values)

def random_quote():
    all_values = read_values_from_json("quotes.json","quote")
    return get_random_item(all_values)

def random_character():
    all_values = read_values_from_json("characters.json","character")
    return get_random_item(all_values)




#Program

user_answer = input("Tapez entrez pour connaitre une autre citation ou B pour quitter le programme")

while user_answer != "B":
    print(message(random_character(), random_quote()))
    user_answer = input("Tapez entrez pour connaitre une autre citation ou B pour quitter le programme")

#github link https://github.com/OpenClassrooms-Student-Center/demarrez_votre_projet_avec_python/blob/P4C1/san_antonio.py








#-------------------------------------
#fonction exemple de turtle -> rosace
#-------------------------------------

#import turtle
#from turtle import *
#color('red', 'yellow')
#begin_fill()
#while True:
    #forward(200)
    #left(170)
    #if abs(pos()) < 1:
        #break
#end_fill()
#done()
