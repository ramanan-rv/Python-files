print("LIST OVERLAP \n")
print("http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html \n")
# List Overlap   
# Exercise 5 (and Solution)
# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
# Extras:
# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
#########################
# Function for generating random lists
import random
def random_list():
  lgt = random.randint(1,11)
  rnd_list=[]
  for i in range(0, lgt):
    rnd_list.append(random.randint(0,100))
  return rnd_list
# End of function
a = random_list()
print ("First list is:", a)
b = random_list()
print ("Second list is:", b)
common_list=[] # initialize a list of common elements
for element in a:
  if element in b:
    if (element in common_list) == False:
      common_list.append(element)
print("The common elements are", common_list)
