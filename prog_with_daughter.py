print("TEACHING / FUN PROGRAMMING WITH MY DAUGHTER \n")
# 
# My daughter was curious about Python programming and wanted to do see how computer will calculate age. So I did this programming without into much details into the time module. 
#
# Ask user for birth day
#
by = int(input("Enter your year of birth: "))
bm = int(input ("Enter your birth month in numbers: "))
bd = int(input ("Enter your birth date: "))
#
# Ask user for today's date
#
ty = int(input("Enter today's year: "))
tm = int(input ("Enter today's month in numbers: "))
td = int(input ("Enter today's date: "))
print ("You said you were born on ", by, bm, bd)
print ("Today is ", ty, tm, td)
age = ty - by
if tm < bm:
  age = age -1
print ("Your age is ", age)
