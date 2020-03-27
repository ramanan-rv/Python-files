print("ROCK PAPERS SCISSORS \n")
# 
# Exercise 8 (and Solution)
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)  
# http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
# 
import random
def play():
  human = input ("Enter r for rock, p for paper or s for scissors.: ")
  if human not in ('r', 'p', 's'):
    print ("Invalid entry, try again")
  else:
    print ("You said ", human)
    computer = random.choice(["r", "p", "s"])
    print ("Computer said ", computer)
    if human == computer:
      print ("Tie!, try again \n")
    elif human == 'p' and computer == 'r':
      print ("You win \n")
    elif human == 'p' and computer == 's':
      print ("Computer wins \n")
    elif human == 'r' and computer == 'p':
      print ("Computer wins \n")
    elif human == 'r' and computer == 's':
      print ("You win \n")
    elif human == 's' and computer == 'p':
      print ("You win \n")
    elif human == 's' and computer == 'r':
      print ("Computer wins \n")
# Main program
print ("Welcome to Rock Papers and Scissors Game \n")
choice =''
while choice != 'q':
  print ("Press q to quit the game or any other key to play \n")
  choice = input()
  if choice == 'q':
    break
  else:
    play()
