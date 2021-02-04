import random

rng = (input("Enter a range of two numbers separated by space: ")).split(" ")
number =  random.randint(int(rng[0]),int(rng[1]))
print('{} is a random number between {} and {}.'.format(number, rng[0], rng[1]))
