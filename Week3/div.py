x =  int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x//y)
reminder = x%y
print('{} divided by {} is {} with riminder {}'.format(x, y, answer,reminder))
