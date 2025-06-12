#----noob starter format for [<ROCK-PAPER-SCISSORS>]-----
print("Rock...")
print("Paper...")
print("scissors...")

player1 = input("player 1,make your move: ")
player2 = input("player 2,make your move: ")

if player1 == "rock" and player2 == "paper":
    print("player2 wins! :) . . .")
elif player1 == "rock" and player2 == "scissors":
    print("player1 wins! :) . . .")
elif player1 == "paper" and player2 == "scissors":
    print("player2 wins! :) . . .")
elif player1 == "paper" and player2 == "rock":
    print("player2 wins! :) . . .")
elif player1 == "scissors" and player2 == "paper":
    print("player1 wins! :) . . .")
elif player1 == "scissors" and player2 == "rock":
    print("player2 wins! :) . . .")
elif player1 == "rock" and player2 == "rock":
    print("its fucking tie!!! :(")
elif player1 == "scissors" and player2 == "scissors":
    print("its fucking tie!!! :(")
elif player1 == "paper" and player2 == "paper":
    print("its fucking tie!!! :(")
else: 
    print("something went wrong")

# ---------updated version of </ROCK-PAPER-SCISSORS\> ------

print("Rock...")
print("Paper...")
print("scissors...")

player1 = input("PLAYER 1, make your move: ")
player2 = input("PLAYER 2, make your move: ")

if player1 == player2:
    print("it's a fucking tie :( ")
elif player1 == "rock":
    if player2 == "scissors":
        print("player1 wins!")
    elif player2 == "paper":
        print("player2 wins !")
elif player1 == "paper":
    if player2 == "rock":
        print("player2 wins! ")
    elif player2 == "scissors":
        print("player2 wins! ")
elif player1 == "scissors":
    if player2 == "paper":
        print("player1 wins! ")
    elif player2 == "rock":
        print("player2 wins! ")
else:
    print("something went wrong!!!!!   :|")

# ---------advanced </ROCK,PAPER,SCISSORS\>--------

from random import randint

player = input("player,make your move: ").lower()
rand_num = randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"

print(f"computer plays {computer}")

if player == computer:
    print("it's a fucking tie :( ")
elif player == "rock":
    if computer == "scissors":
        print("player wins :)!")
    elif computer == "paper":
        print("computer wins :]!")
elif player == "paper":
    if computer == "rock":
        print("computer wins! :] ")
    elif computer == "scissors":
        print("computer wins! :] ")
elif player == "scissors":
    if computer == "paper":
        print("player wins! :) ")
    elif computer == "rock":
        print("computer wins! :] ")
else:
    print("something went wrong!!!!!   :|")

