# This program reads an number and prints if it is even or odd 

num = int(input('Enter a number (-1 to quit): '))
while num != -1:
    if (num%2 == 0):
        print(f"Number {num} is even")
    else:
        print(f"Number {num} is odd")
    num = int(input('Enter a number (-1 to quit): '))   