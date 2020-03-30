# Fibonacci
# http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
# Exercise 13 (and Solution)
# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fibonacci(num):
    if num == 0:
        seq = []
    elif num == 1:
        seq = [1]
    else:
        seq = [1,1]
        while len(seq)< num:
            ult_num = seq[len(seq)-1]
            pen_num = seq[len(seq)-2]
            new_element = ult_num + pen_num
            seq.append(new_element)
    return seq
how_many = int(input("How many numbers of Fibonnaci sequence do you want to be generated? \n"))
my_list= fibonacci(how_many)
print ("Your list is: ", my_list, "\n")
