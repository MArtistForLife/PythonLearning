##---------------------##
print("EXERCISE 1")
print("Now we need to explore scopes through the lens of a wall around a garden(?).")

enemies = 1

def increaseEnemies():
    global enemies #make the variable called enemies a global one whose internal form can be called externally (outside function)
    #return enemies + 1
    enemies += 1 
    print(f"enemies inside function: {enemies}") #now that enemies has been made global, its value inside function = retained outside
    #if this print statement comes before the line enemies += 1, it will still go with one because the print occurs before addition

increaseEnemies() #call the function
print(f"enemies outside function: {enemies}") #why are we doing this twice? loll

#okay this is why...
#INSIDE the function, we have enemies defined as 2
#but OUTSIDE the function, enemies is defined as 1
#based on the scope of things, if we have a print statement for enemies INSIDE the function, it'll go with the internal 2
#but OUTSIDE of the function, having a print statement will just show the external 1

#local scope
# def drinkPotion():
#     potionStrength = 2
#     print(potionStrength)

#drinkPotion()
#print(potionStrength) #this won't work because potionStrength is only defined INSIDE the function drinkPotion(), not OUTSIDE it

#global scope
# playerHealth = 10

# def game():
#     def drinkPotion():
#         potionStrength = 2
#         print(playerHealth)
    
#     drinkPotion()

# print(playerHealth)

#there's no block scope here
# if 3 > 2:
#     someVariable = 10 #wtf is the point of this line?

# gameLevel = 3
# def createEnemy():
#     allEnemies = ["Skeleton", "Zombie", "Alien"]
#     if gameLevel < 5:
#         newEnemy = allEnemies[0]

# print(newEnemy) #this doesn't work because it is outside the function, hence outside the local scope of that function

##---------------------##
print("\nEXERCISE 2")

PI = 3.14159
URL = "https://www.google.com"
INSTAGRAM_HANDLE = "@staytinyvibes"

def calc():
    print(PI)
calc()

##---------------------##
print("\nEXERCISE 3")
import random

print("Welcome to the Number Guessing Game!\n\nI'm thinking of a number between 1 and 100.")

#while loop will go till attempts are done
def numberGame(tries, num):
    while tries > 0:
        if tries > 1:
            guess = input(f"You have {tries} attempts remaining to guess the number. \nMake a guess: ")
        elif tries == 1:
            guess = input(f"You have {tries} attempt remaining to guess the number. \nThink carefully and make a guess: ")
        
        #just in case something wacky gets typed up
        while not guess.isdigit() and guess.strip() != "":
            guess = input("Whoops, invalid! Please type an integer: ")

        if guess.isdigit():
            guess = int(guess)
        else:
            print("You didn't write an number. Please write one.")
            continue

        if guess > num:
            tries -= 1
            if tries > 0:
                print("Too high. Guess again.")
        elif guess < num:
            tries -= 1
            if tries > 0:
                print("Too low. Try again.")
        elif guess == num:
            print("Yay, you got it!")
            return
    print(f"Yikes, you've run out of attempts. The number was {num}.")

while True:
    #to decide difficulty level for the game
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        attemptsLeft = 10
    elif difficulty == "hard":
        attemptsLeft = 5
    else:
        while difficulty not in ["easy", "hard"]:
            difficulty = input("Whoops, invalid answer. Please type 'easy' or 'hard': ")
        attemptsLeft = 10 if difficulty == "easy" else 5

    thoughtNumber = random.randint(1, 101) #picks a random number in that range
    #gameOver = False
    numberGame(attemptsLeft, thoughtNumber)
    
    option = input("Do you want to play a number game? Type 'yes' or 'no': ")
    if option == "yes":
        continue
    elif option == "no":
        print("Alright then, maybe next time! :)")
        break
    else:
        print("Whoops, invalid response. please type 'yes' or 'no': ")








