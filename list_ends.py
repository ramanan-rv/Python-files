# List Ends
# Exercise 12 (and Solution)
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

def make_list():
    mklist=[]
    quit = ""
    while quit != 'q':
        mklist.append(int(input("Enter numbers to the list.\n")))
        quit = input("Enter q to quit or any key to continue \n")
    return mklist
def list_ends(list1):
    fl_list = [list1[0], list1[len(list1)-1]]
    return fl_list
    
my_list = make_list()
result = list_ends(my_list)    
print ("Your list is: ", my_list, "\n")
print ("List with first and last elements is: ", result, "\n")
