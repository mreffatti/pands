# This program reads in a student percentage and prints out the coresponding grade as follows

#Under 40% => Fail
#Between 40% and 49% => Pass
#Between 50% and 59% => Merit 2
#Between 60% and 69% => Merit 1
#Over 70% => Distinction

percentage = float(input("Enter the Percentage: "))

if percentage < 0 or percentage > 100:
    print ("Please enter a number between 0 and 100.")
elif percentage < 40:
    print("Fail")
elif percentage < 50:
    print("Pass")
elif percentage < 60:
    print("Merit 2")
elif percentage < 70:
    print("Merit 1")
else:
    print("Distinction")

