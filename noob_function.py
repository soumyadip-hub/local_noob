# ---------FUNCTION-------
def sing_happy_birthday():
    print("happy birthday to you")
    print("happy birthday to you")
    print("happy birthday dear to you")
    print("Happy birthday To You")

sing_happy_birthday()
sing_happy_birthday()
sing_happy_birthday()

#-----------coin_flip function-----

from random import random

def flip_coin():
    #genearte random number between 0-1
    r=random()
    if r > 0.5:
        return"Heads"
    else:
        return "Tails"
 
print(flip_coin())

#using parameters------

def square(num):
    return num * num
print(square(4))
print(square(5))