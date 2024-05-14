print("EXERCISE 1")
a=123
print(type(a)) #results in <class 'int'>
b=str(123)
print(type(b)) #results in <class 'str'>
c=float(123)
print(type(c)) #results in <class 'float'>
print(70 + float("100.5")) #returns 170.5
print(str(70)+str(100)) #returns 70100

print ("EXERCISE 2")
twoDigitNumber = input()
sum = int(twoDigitNumber[0]) + int(twoDigitNumber[1])
print(sum)

print("EXERCISE 3")
height = input("What is your height in meters? ")
weight = input("What is your weight in kilograms? ")
bmi = float(weight) / (float(height)**2)
finalBMI = int(bmi)
print(finalBMI)

print("EXERCISE 4")
age = float(input("What is your age in years (use decimals if needed)? "))
years = 90.0 - age
weeks = years * 52
print(f"I am {age} years old, so if I live to be 90, I have {weeks} weeks left.")

print("EXERCISE 5")
print("Welcome to the tip calculator!")
total = input("What was the total bill? ")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = int(input("How many people to split the bill? "))
divvy = float(total) * (1.0 + (float(tip)/100)) / people
finalDivvy = round(divvy, 2) #rounds amount for each person to the nearest cent, that is, 2 decimal places
print(f"Each person should pay ${finalDivvy}.")