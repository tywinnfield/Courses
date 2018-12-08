# EX 1
"""a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

user_input = input("Entrez un chiffre")
user_input = int(user_input)

for i in a :
    if i < user_input:
        new_list.append(e)
        
print(new_list)

"""
# EX 4

"""
# boucle de validation de l'input

i= 1
while i == 1:
    user_input = input("enter a number: ")
    try:
        user_input = int(user_input)
        assert user_input > 0
    except TypeError:
        print("Veuillez entrer un nombre entier")
    except AssertionError:
        print("Veuillez entrer un nombre entier positif")
    except ValueError:
        print("Veuillez entrer un nombre entier")
    else:
        i = 0
        print("c'est parti !")

list = []

# boucle de calcul de diviseur et append list
for e in range(1, user_input+1):
    if user_input % e  == 0:
        list.append(e)
print(list)

# correction 
num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num % number == 0 :
        divisorList.append(number)
print(divisorList)

"""

#EX 5

"""

import random
a = random.sample(range(1,100), 35)
b = random.sample(range(1,100), 25)
list = []

#find common num
for e in a:
    if e in b:
        if e not in list:
            list.append(e)
print(list)"""

# EX 6

"""
word = input("enter a word ")
word = str(word)

drow = word[::-1]
print(drow)

if word == drow :
    print("palindrome")
else:
    print("fail")

"""

# EX 7

"""
import random
a = random.sample(range(1,100), 10)
print(a)
b = [i for i in a if i % 2 == 0]

print(b)

"""

#EX 8

"""
print("the game is on !")
i = 1
while i == 1:
    player_1 = input("Player 1, what do you play ? Rock, Paper or Scissors ? ")
    player_2 = input("Player 2, what do you play ? Rock, Paper or Scissors ? ")
    if player_1 == "Rock" and player_2 == "Scissors" or player_1 == "Scissors" and player_2 == "Paper" or player_1 == "Paper" and player_2 == "Rock":
            print("Player 1 WINS ! congratulations")
    elif player_2 == "Rock" and player_1 == "Scissors" or player_2 == "Scissors" and player_1 == "Paper" or player_2 == "Paper" and player_1 == "Rock":
            print("Player 2 WINS ! congratulations")
    else:
            print("Draw ! Nobody wins !")
        
    print("Voulez vous rejouer ? OUI ou NON")
    decision = input()
    if decision == "OUI":
        i = 1
    elif decision =="NON":
        i = 0
        print("Très bien on arrête")
    else:
        print("Nous n'avons pas compris")

"""

# EX9 à améliorer

"""
import random

print("Nous allons jouer aux devinettes ! C'est parti !")
a = random.randint(1, 10)
guess = int(input("Veuillez donner un chiffre entre 1 et 9 : "))
guess_num = 1

i = 1
while i == 1:
         
    if guess < a:
        print("It's higher")
        print("Do you want to try again ? YES or No")
        decision = input()
        if decision == "YES":
            guess_num +=1
            guess = int(input("Veuillez donner un chiffre entre 1 et 9 : "))
        else:
            i = 0
            print("The game is finished. You needed %d attempts" % guess_num)
        
    elif guess > a:
        print("It's lower")
        print("Do you want to try again ? YES or No")
        decision = input()
        if decision == "YES":
            guess_num +=1
            guess = int(input("Veuillez donner un chiffre entre 1 et 9 : "))
        else:
            i = 0
            print("The game is finished. You needed %d attempts" % guess_num)
            
    else:
        guess == a
        print("Bravo !! Great guess !!")
        i = 0
        print("The game is finished. You needed %d attempts" % guess_num)"""

#EX 10

"""
import random
a = random.sample(range(1,10), 4)
b = random.sample(range(1,10), 5)
list = []

list = [e for e in set(a) if e in b ]
print(list)

"""
            
# EX 11

# correction
"""
num = int(input('Insert a number : '))
a = [ x for x in range(2, num) if num % x == 0]

def is_prime(n):
    if num > 1:
        if len(a) == 0:
            print('prime')
        else:
            print('not prime')
    else:
        print('not prime')

is_prime(num)

"""

# EX 12

import random

a = random.sample(range(1,10), 5)
b = []

def first_last():
    b = [a[0], a[-1]]
    return b

print(first_last())


# EX 13

# write a program that asks user how many Fibonacci numbers to generate and generates them.


num = input(" how many fibo numbers do you want ? ")

fibo_nums = []

def fibo():
    x = 0
    y = 1
        
print(fibo())

        




                



