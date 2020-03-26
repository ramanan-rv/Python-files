print("LIST COMPREHENSIONS \n")
print("http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html \n")
# Exercise 7 (and Solution)
# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
#########################
import random
a = [random.randint(0,100) for x in range (0, 10)] # create a random list
new =[x for x in a if x%2 ==0] # make a filtered list of even numbers from list a
print (a, 2*"\n", new)
