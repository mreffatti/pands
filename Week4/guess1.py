import random
num = random.randint(0,100)

guess = int(input("Guess a number between 0 and 100 (-1 to quit) "))

while  guess != -1:
    if guess == num:
        print("You got it")
        break
    else:
        print("Please try another number")
        guess = int(input("Guess a number between 0 and 100 (-1 to quit)"))

print(f"The number was {num}.")
