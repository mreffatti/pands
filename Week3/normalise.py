rawString = input("Enter a string: ")
normalizedString = rawString.strip().lower()

lenRaw = len(rawString)
lenNorm = len(normalizedString)


print(f'That string normalized is: {normalizedString}')
print(f'We reduced the input string from {lenRaw} to {lenNorm} characters.')