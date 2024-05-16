##---------------------##
print("EXERCISE 1")
#importing random to generate random integers
import random
randomInteger = random.randint(1, 10) #generates a random integer between 1 and 10
print(randomInteger)

#testing importing a file from the same folder and calling a value defined in that other file
import maths #imports the file called maths.py, which is in the same folder as this file called lists.py
print(maths.pi) #prints the value of pi as defined in the file called maths.py

#to generate a random float number
randomFloat = random.random() * 5 #generates a random number in the interval [0, 1), and times by 5 in case it's something like 0.0001...
print(randomFloat)

print("We can make something randomized like this:")
loveScore = random.randint(1, 100) #generates random number between 1 and 100
print(f"Your love score is {loveScore}.")
##---------------------##
print("\nEXERCISE 2")
print("Now we are going to play a game of Heads or Tails.")
randomCoin = random.randint(0, 1)
if randomCoin == 0:
    print("Heads")
if randomCoin == 1:
    print("Tails")
##---------------------##
print("\nEXERCISE 3")
USAstates = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(USAstates[0])

#suppose you decide to spell Pennsylvania as "Pencilvania"; you can change that
# USAstates[1] = "Pencilvania"
# print(USAstates) #the change to Pencilvania will be included now

#to add a new item to the list:
# USAstates.append("Monkeyland")
# print(USAstates)

#to add MULTIPLE items to the list:
# USAstates.extend(["Jumpyworld", "Highfivers"])

stateCount = len(USAstates)
print(f"There are {stateCount} states.")
print(f"The last state in the list, the one that joined the union last, is {USAstates[stateCount-1]}.")
print(USAstates)
##---------------------##
print("\nEXERCISE 4")
nameTally = "Angela, Ben, Jenny, Michael, Chloe"
names = nameTally.split(", ") #separates the string into separate names, puts into list, and separates by commas
#so, if your input is x, y, z, then names = ["x", "y", "z"]
itemCount = len(names) #gets the number of items in list
randomChoice = random.randint(0, itemCount - 1) #range is 0 (index start point), and -- IMPORTANT -- the variable - 1 (index end point)
print(f"{names[randomChoice]} will pay the bill this round.") #to pick a random name
##---------------------##
print("\nEXERCISE 5")
#dirtyDozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

#from this make two lists that distinguishes the fruits from the vegetables
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes"]
vegetables = ["Spinach", "Kale", "Celery", "Potatoes"]

dirtyDozen = [fruits, vegetables] #group together the two lists into one of the dirty dozen
print(dirtyDozen) #returns two pairs of brackets within brackets because they are two lists

##---------------------##
print("\nEXERCISE 6")
line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? A1, B1, C1, A2, B2, C2, A3, B3, or C3? ")

letter = position[0].lower() #you have a letter from the first input and make it lowercase
abc = ["a", "b", "c"]
letterIndex = abc.index(letter) #checks if, within the list abc, we have some letter existing, and the position (index) of it
numberIndex = int(position[1]) - 1 #checks the second digit in the inputted position (i.e., a number) and subtracts 1 since counting starts at 0
#because, position 3 is actually number 2

map[numberIndex][letterIndex] = "x" #have numberIndex before letterIndex because with nested lists you go from OUT to IN (i.e., backwards in a way)
print(f"{line1}\n{line2}\n{line3}")

##---------------------##
print("\nEXERCISE 7")
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
               ______)
              _______)
             _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
              ______)
           __________)
          (____)
---.__(___)
"""

#player choice
choice = int(input("Let's play a game of rock, paper, scissors. What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if choice >= 3 or choice < 0:
    print("Invalid number, you lose!")
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)

#computer choice
pc = random.randint(0, 2) #always use the random module when you want to randomize something in a numerical range
print(f"The computer chose {pc}.")
if pc == 0:
    print(rock)
elif pc == 1:
    print(paper)
elif pc == 2:
    print(scissors)

#to decide winner of the game; 0 = rock, 1 = paper, 2 = scissors
#0 beats 2, 1 beats 0, and 2 beats 1
if choice == str(pc):
    print("It's a draw!")
elif (choice == 0 and pc == 2) or (choice == 1 and pc == 0) or (choice == 2 and pc == 1):
    print("You win!")
elif (pc == 0 and choice == 2) or (pc == 1 and choice == 0) or (pc == 2 and choice == 1):
    print("The computer wins!")