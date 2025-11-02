"""Number game
Outline:
Write a program to generate a random integer and match it with the input given by the user?"""

import random
playing=True
number=str(random.randint(10,20))
print("I will generate a number from 10 to 20 and you have to guees the number")
print("The game ends when you guess the number,you need to guess one number at a time")
while playing:
    guess=input("Give me your best guess! :") 
    if number==guess:
        print("You won the game")
        print("The number was",number)
        break
    else:
        print(ValueError,"Wrong answer try again")



"""Rock paper scissors
Outline:
Create a program to play rock, paper, and scissors. Use a random module to select from 
the given options Check whether the random guess matches the user's answer"""

import random
while True:
    user_action=input("Pick your move,rock,paper,or scissors:")
    possible_actions=["rock","paper","scissors"]
    computer_action=random.choice(possible_actions)
    print(f"You chose {user_action},computer chose {computer_action}.")
    if user_action==computer_action:
        print(f"Both players selected {user_action}.It's a tie!")
    elif user_action=="rock":
        if computer_action=="scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose!")
    elif user_action=="paper":
        if computer_action=="rock":
            print("Paper covers rock! You win!")
        else:
           print("Scissors cut paper! You lose!")
    elif user_action=="scissors":
        if computer_action=="paper": 
            print("Rock smashes scissors! You lose!") 
    play_again=input("Play again? (yes or no):")
    if play_again!="yes":
        break



    """Mathematical operations
Outline:
Write a program to understand the different functions of the math module."""

import math
print(math.sqrt(16))