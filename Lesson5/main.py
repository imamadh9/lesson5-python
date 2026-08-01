# Lesson 5 - Rock, Paper, Scissors
import random

choices = ["rock", "paper", "scissors"]
computer_count = 0
player_count = 0

again = "yes"

while again == "yes":
    player = input("Please enter rock, paper or scissors: ").lower()
    if player not in choices:
        player = input("Invalid input. Try again: ")

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if player == computer:
        print("Tie!")
    elif((player == "rock" and computer == "paper")
         or (player == "paper" and computer == "scissors")
         or (player == "scissors" and computer == "rock")):
        print("Computer won!")
        computer_count = computer_count + 1
    else:
        print("You won!")
        player_count = player_count + 1
    print("Computer:", computer_count)
    print("You:", player_count)
    print()
    again = (input("Play again? (yes/no): ")).lower()