# Check Primality Functions
# Exercise 11 (and Solution)
# Ask the user for a number and determine whether the number is prime or not. 
# You can (and should!) use your answer to Exercise 4 to help you. 
# Take this opportunity to practice using functions, described below.
def chk_prime(num):
    divisor = 2
    if num == 1:
        print ("1 is neither prime not composite. \n")
    else:
        while divisor <= num:
            divides = num%divisor
            if divides == 0 and divisor < num:
                print (num, "is not prime. \n")
                break
            if divides == 0 and divisor == num:
                print (num, "is prime. \n")
            divisor+=1
    return
print ("Check if number is prime. \n")
print ("Source: http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html \n")
nbr = int(input ("Enter a number to check if prime or 0 to quit. \n"))
while nbr != 0:
    chk_prime(nbr)
    nbr=int(input("Enter 0 to quit, or any other number  to continue checking. \n"))
    
