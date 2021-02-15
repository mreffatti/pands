numberOfQuestions = 5
averageAge = 23.4
debugMode = True
name = "joe"
ages = []
months = ('Jan', 'Feb', 'Mar')
book = {}
stuff = [ 12 , 'Fred', False, {}]
someone = dict(firstname = "joe")
me = {"firstName" : "Andrew", "teaching" : [{ "courseName" : "programming", "semester" : 1 },{ "courseName" : "Data Representation", "semester" : 2 }]}


print(f'a. {type(numberOfQuestions)}')
print(f'b. {type(averageAge)}')
print(f'c. {type(debugMode)}')
print(f'd. {type(name)}')
print(f'e. {type(ages)}')
print(f'f. {type(months)}')
print(f'g. {type(months[1])}')
print(f'h. {type(book)}')
print(f'i. {type(stuff)}')
print(f'j. {type(stuff[2])}')
print(f'k. {type(someone)}')
print(f'l. {type(someone["firstname"])}')
print(f'm. {type(me)}')
print(f'n. {type(me["teaching"])}')
print(f'o. {type(me["teaching"][0]["semester"])}')
print(f'p. {type(me["teaching"][0]["courseName"])}')
