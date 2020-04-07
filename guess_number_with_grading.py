# This is a guess the number name.

def grading (trails):
    if tries == 1:
        print ("BINGO!", name, "That was an awesome stroke of luck! \n")
    elif tries < 5:
        print ("Good job!", name, "You took", tries, "guesses. An optimal strategy or was it luck? \n")
    elif tries <9:
        print ("That's correct.", name, "You took", tries, "guesses. \n")
    else:
        print (name, "You took", tries, "guesses. Could be better though. \n")

import random

print ("Hello! what is your name?\n")
name = input()

print ("Hello", name, ", I am thinking of a number between 1 to 20. \n")
secretNumber = random.randint(1,20)
print("Enter the number I am guessing. \n")

wrong = True # Set the flag for the correctness of the user guess. 
tries = 1    # Initialize the trail number to 1 for the first try.

while wrong:    # Loop as long guesses are wrong
    guess = int(input())
    if guess > secretNumber:
        print("Your guess is high. Try again. \n")
    elif guess < secretNumber:
        print("Your guess is low. Try again. \n")
    else:
        grading (tries) # Use grading () function to grade based on number of trails. 
        wrong = False   # Set wrong flag to False to exit the loop. 
    tries+=1
