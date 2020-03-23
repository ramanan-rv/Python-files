name = input("Give me your name: ")
age = int(input("Give me your age: "))
year_at_100 = (100-age)+2020
print_msg = f"Hi {name}, you will be 100 years old in {year_at_100} \n"
print (print_msg)
times = int(input("How many times do you want this message to be printed: "))
print(times * print_msg)
