import random
num = random.randint(0,100)

guess = int(input("Guess a number between 0 and 100 (-1 to quit) "))

while  guess != -1:
    if guess == num:
        print("You got it")
        break
    else:
        if guess < num:
            print("Too low -  Please try a higher number")
        else:
            print("Too high -  Please try a lower number")

        guess = int(input("Guess a number between 0 and 100 (-1 to quit)"))

print(f"The number was {num}.")