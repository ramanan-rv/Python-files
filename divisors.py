print("DIVISORS \n")
print("Source:http://www.practicepython.org/exercise/2014/02/26/04-divisors.html \n")
# Divisors   
# Exercise 4 (and Solution)
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
num = int(input("Enter a number to find its divisors: "))
divisor=[] # initialize a list of divisors of the number
for i in range(1, num+1):
  if num%i == 0:
    divisor.append(i)
print("The divisors of ", num, "are", divisor)
