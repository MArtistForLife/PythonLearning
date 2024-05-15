print("EXERCISE 1")
print("Welcome to the rollercoaster!")
height = float(input("What is your height in cm? "))
if height >= 120.0:
    print("You can ride the rollercoaster!")
    age = float(input("What is your age in years? "))
    if age < 12.0:
        cost = 5
        print("Child tickets are $5.")
    elif age <= 18.0:
        cost = 7
        print("Youth tickets are $7.")
    elif age >= 45.0 and age <= 55.0:
        cost = 0
        print("It's alright, you can go for free!")
    else:
        cost = 12
        print("Adult tickets are $12.")
    photos = input("Do you want a photo taken? Yes or No. ")
    if photos == "Yes" or photos == "yes":
        cost += 3
        print(f"Your total is ${cost}.")
    if photos == "No" or photos == "no":
        cost = cost
        print(f"Your total is {cost}.")
else:
    print("Sorry, you have to grow taller before you can ride.")

print("\nEXERCISE 2")
number = int(input("Write a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

print("\nEXERCISE 3")
height = float(input("What is your height in m? "))
weight = float(input("What is your weight in kg? "))
bmi = weight / (height**2)
if bmi < 18.5:
    print("You are underweight.")
elif bmi >= 18.5 and bmi < 25.0:
    print("You have a normal weight.")
elif bmi >= 25.0 and bmi < 30.0:
    print("You are slightly overweight.")
elif bmi >= 30.0 and bmi < 35.0:
    print("You are obese.")
else:
    print("You are clinically obese.")

print("\nEXERCISE 4")
year = int(input("Write a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year!")
        elif year % 400 != 0:
            print(f"Huh, {year} is not a leap year.")
    elif year % 100 != 0:
        print(f"{year} is a leap year!")
else:
    print(f"Huh, {year} is not a leap year.")

print("\nEXERCISE 5")
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? Small, Medium, or Large. ")
pepperoni = input("Do you want pepperoni? Yes or No. ")
cheese = input("Do you want extra cheese? Yes or No. ")
if size == "Small" or size == "small":
    cost = 15
    if pepperoni == "Yes" or pepperoni == "yes":
        cost += 2
    if cheese == "Yes" or cheese == "yes":
        cost += 1
elif size == "Medium" or size == "medium":
    cost = 20
    if pepperoni == "Yes" or pepperoni == "yes":
        cost += 3
    if cheese == "Yes" or cheese == "yes":
        cost += 1
elif size == "Large" or size == "large":
    cost = 25
    if pepperoni == "Yes" or pepperoni == "yes":
        cost += 3
    if cheese == "Yes" or cheese == "yes":
        cost += 1
print(f"Your total is ${cost}.")

print("\nEXERCISE 6")
print("The Love Calculator is calculating your score...")
name1 = input("Write one person's name: ")
name2 = input("Write another person's name: ")
together = name1+name2
lowercase = together.lower()
t = lowercase.count("t") #checks both names for if there is a letter "t"
r = lowercase.count("r") #and vice versa
u = lowercase.count("u") 
e = lowercase.count("e")
firstDigit = t+r+u+e
l = lowercase.count("l") 
o = lowercase.count("o")
v = lowercase.count("v") 
e = lowercase.count("e")
secondDigit = l+o+v+e
compatible = int(str(firstDigit) + str(secondDigit))
if compatible < 10 or compatible > 90:
    print(f"Your score is {compatible}, you go together like coke and menthos.")
elif compatible >= 40 and compatible <= 50:
    print(f"Your score is {compatible}, you are alright together.")
else:
    print(f"Your score is {compatible}, you have strong potential together.")

print("\nEXERCISE 7")
print("Welcome to Treasure Island. Your mission is to find the treasure.")
direction = input("You come to a fork in the road. Where do you go, left or right? ")
if direction == "Right" or direction == "right":
    print("Game Over.")
if direction == "Left" or direction == "left":
    nextAction = input("You reach a river that has a boat ride every 20 minutes. Do you swim or wait? ")
    if nextAction == "Swim" or nextAction == "swim":
        print("Game Over.")
    if nextAction == "Wait" or nextAction == "wait":
        finalAction = input("You come to a set of three doors, all different colors. Which door do you open: red, yellow, or blue? ")
        if finalAction == "Red" or finalAction == "red":
            print("The room is full of fire! Game Over.")
        elif finalAction == "Blue" or finalAction == "blue":
            print("You are flooded by a tidal wave. Game Over.")
        elif finalAction == "Yellow" or finalAction == "yellow":
            print("Congratulations! You find the treasure and win!")