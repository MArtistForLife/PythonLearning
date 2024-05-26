##---------------------##
print("EXERCISE 1")

# def someFunction():
#     for number in range(1, 20):
#         if number == 20:
#             print("You got it!")
# someFunction()
#~~the above will NOT print the statement because the rannge means you can only go up to 19, not 20

#fixed
def someFunction():
    for number in range(1, 21):
        if number == 20:
            print("You got it!")
someFunction()

##---------------------##
print("\nEXERCISE 2")

# from random import randint
# diceImages = ["(1)", "(2)", "(3)", "(4)", "(5)", "(6)"]
# diceNumbers = randint(1,6)
# print(diceImages[diceNumbers])
#~~the indexing needs to be correct here -- 0 to 5, NOT 1 to 6

from random import randint
diceImages = ["(1)", "(2)", "(3)", "(4)", "(5)", "(6)"]
diceNumbers = randint(0,5) #use correct indexing here, too
print(diceImages[diceNumbers]) #this will get the "image" that is at the index number of the random number

##---------------------##
print("\nEXERCISE 3")

# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")

year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994: #need to include 1994 and not exclude it out of either ranges presented here
    print("You are a Gen Z.")

##---------------------##
print("\nEXERCISE 4")

# age = input("How old are you? ")
# if age > 18:
#     print("You can drive at age {age}.")

age = int(input("How old are you? ")) #cast the string to an INTEGER
if age > 18:
    print(f"You can drive at age {age}.") #need f-string!!

##---------------------##
print("\nEXERCISE 5")

pages = 0
wordPerPage = 0
pages = int(input("Number of pages: "))
print(f"Our page number is {pages}.")

wordsPerPage = int(input("Number of words per page: "))
print(f"Our words per page count is {wordsPerPage}.")

totalWords = pages * wordsPerPage
print(f"Given this page number and words per page, you got {totalWords} words in total.")

##---------------------##
print("\nEXERCISE 6")

def mutate(someList):
    nextList = []
    for item in someList:
        newItem = item*2
        nextList.append(newItem) #make sure this is indented so that it is included in the for loop
    print(nextList)

mutate([1,2,3,5,8,13])

##---------------------##
print("\nEXERCISE 7")
#this is from lesson 3, managing data

# number = int(input("Write a number: "))
# if number % 2 == 0:
#     print(f"{number} is an even number.")
# else:
#     print(f"{number} is an odd number.")

#what if something not an integer is typed??

while True: #creates infinite loop that will keep asking for input until a valid number (i.e., an integer) is given
    try: #attempts to convert input into an integer
        number = int(input("Write a number: "))
        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")
        break #exit the infinite loop of while True if an integer is given 
    except ValueError: #catches error if input is NOT an integer, and then can print the following error message
        print("Whoops, that's not an integer. Try again :)")

##---------------------##
print("\nEXERCISE 8")
#this is also from lesson 3, the leap year shenanigans

# year = int(input("Write a year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year!")
#         elif year % 400 != 0:
#             print(f"Huh, {year} is not a leap year.")
#     elif year % 100 != 0:
#         print(f"{year} is a leap year!")
# else:
#     print(f"Huh, {year} is not a leap year.")

# i need to add a section for dealing with value errors

while True: #infinite loop
    try:
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
        break #breaks the infinite loop IF a valid number (in this case, an integer) is given
    except ValueError:
        print("whoops, that's not an integer. Try again!")