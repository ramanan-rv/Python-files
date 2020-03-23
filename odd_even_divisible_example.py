print("ODD OR EVEN EXAMPLE \n")
print("Source:http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html \n")
input()
num = int(input("Enter a number to check even or odd: " ))
check = int(input("Enter a number to divide that number: "))
if num%2 == 0:
  print(num, "is even")
  if num%4 == 0:
    print(num, "is also a multiple of 4")
else:
  print(num, "is odd")
if num%check ==0:
  print(num, "is divisible by", check)
else:
  print(num, "is not divisible by", check)
