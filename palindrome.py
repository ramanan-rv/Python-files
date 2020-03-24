print("PALINDROME \n")
print("http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html \n")
# String Lists (Palindrome)  
# strings lists index 
# Exercise 6 (and Solution)
# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
#########################
# This program compares itself without creating a new reverse string
string = input("Please enter a string: ")
length = (len(string))
i=0
while i <= int(length/2): # run iteration to half the string length
  if string[i] != string[-1-i]: # compare the string elements from opposite ends, going inwards
    print ("The string ", string, " is not a palindrome")
    break
  else:
    print ("The string ", string, " is a palindrome")
    break
