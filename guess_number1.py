print ("Guessing Game One \n")
# http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html  
#Exercise 9 (and Solution)
#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
#Extras:
#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random
quit = "no"
counter = 0
correct = 0
while quit != "yes":
  counter += 1
  rnd = random.randint(1,9)
  guess = int(input("Guess the number, between 1 and 9, I have. \n"))
  if guess == rnd:
    print ("You guessed it right!\n")
    correct += 1
  elif guess > rnd:
    print ("Your guess was high by", guess - rnd, "\n")
  else:
    print ("Your guess was low by", rnd - guess, "\n")
  quit = input("Type yes to quit \n")
  if quit != "yes":
    print("\n Continuing.... \n")
print ("You got ", correct, "correct out of", counter, "\n")
print ("Bye")
