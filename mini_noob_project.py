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