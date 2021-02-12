import random

lst = []

while len(lst) < 10:
    num = random.randint(0,100)
    lst +=[num]

print(f"{len(lst)} randon numbers: \t {lst}")
lst.sort(reverse=True)
print(f"The top 3 are: \t\t {lst[0:3]}")