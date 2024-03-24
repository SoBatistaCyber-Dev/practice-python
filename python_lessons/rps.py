# rps stands for rock, paper, scissors
import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

while(True):
    print("")
    playerchoice = input("Enter...\n1 for Rock,\n2 for Paper or \n3 for Scissors:\n0 Exit\n")

    player = int(playerchoice)

    if player < 0 or player > 3:
        sys.exit("You must enter 0, 1, 2 or 3.")

    if player == 0:
        print("Bye bye")
        break

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("")
    print("You chose " + str(RPS(player)).replace('RPS.','') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.','') + ".")
    print("")

    if RPS(player) == RPS.ROCK and RPS(computer) == RPS.SCISSORS:
        print("You win!")
    elif RPS(player) == RPS.PAPER and RPS(computer) == RPS.ROCK:
        print("You win!")
    elif RPS(player) == RPS.SCISSORS and RPS(computer) == RPS.PAPER:
        print("You win!")
    elif player == computer:
        print("Tie game!")
    else:
        print("Python wins!")