#IDLE Open Source
#Note to Viewer: Notes given in between functions
#Jeremy Luo


import random

# Ask the user to choose between Rock, Paper, or Scissors
user_choice = input("Rock, Paper, Scissors\nRock, paper, or scissors? ").lower()

# Translate the user's choice to a number so it is easier for the computer to understand 
if user_choice == "rock":
    user_choice_num = 0
elif user_choice == "paper":
    user_choice_num = 1
elif user_choice == "scissors":
    user_choice_num = 2
else:
    print("That is not a valid option. Please try again!")
    exit()

# Generate the computer's choice as a random number between 0 and 2 (since we translated user input to numbers from 0 to 2)
computer_choice_num = random.randint(0, 2)

# Translate the computer's choice from a number to the corresponding string (rock, papper, or scissors)
if computer_choice_num == 0:
    computer_choice = "rock"
elif computer_choice_num == 1:
    computer_choice = "paper"
elif computer_choice_num == 2:
    computer_choice = "scissors"

# Determine the winner of the game based on the rules of the game given
if user_choice_num == computer_choice_num:
    print(f"The computer played {computer_choice}.\nYou tie!")
elif (user_choice_num - computer_choice_num) % 3 == 1:
    print(f"The computer played {computer_choice}.\nYou win!")
else:
    print(f"The computer played {computer_choice}.\nYou lose!")

