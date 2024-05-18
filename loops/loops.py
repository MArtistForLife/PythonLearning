##---------------------##
print("EXERCISE 1")
fruits = ["Apple", "Peach", "Pear"] #make a list of fruit
for fruit in fruits:
    print(fruit) #for any item(s) in the list called fruits, print the item(s)
    #this for loop allows us to execute the print statement 3 times, that is, as a loop
    print(fruit + " Pie") #this is the 2nd command that the for loop will run for each item in the list
print(fruits) #outside the for loop due to the lack of an indent here

##---------------------##
print("\nEXERCISE 2")
print("Let's find the average height of a group of students.")

#input heights
studentHeight = []
while True:
    heightInput = input("Type a height to the nearest cm, or type 'done' to be finished: ")
    if heightInput.lower() == "done":
        break #exit the for loop if user types "done"
    studentHeight.append(int(heightInput)) #add the inputted heights to list
print(f"The total height is {sum(studentHeight)} cm.")

#calculate total height using for loop
totalHeight = 0
for height in studentHeight:
    totalHeight += height #the total height is acquired by accumulating any value in studentHeight

#calculate number of students using for loop
studentCount = 0
for student in studentHeight:
    studentCount += 1 #add to student count every time there is a value in the studentHeight list

#calculate avg height using total height and student count
if studentCount > 0:
    averageHeight = round(totalHeight/studentCount)
else:
    averageHeight = 0

print(f"The average height is {averageHeight} cm.")

##---------------------##
print("\nEXERCISE 3")
print("Let's find the highest score from a list of student test grades.")

#to input student scores into a list
studentScores = []
while True:
    gradeInput = input("Type a test score to the nearest integer, or type 'done' to be finished: ")
    if gradeInput.lower() == "done":
        break #stop the for loop once "done" is written
    studentScores.append(int(gradeInput))

#to accumulate student scores into the total
totalScores = 0
for score in studentScores:
    totalScores += score

#to find the highest grade in the list without the min or max function
highest = studentScores[0] #we assume the first grade in the list is the highest

#now we go through the list starting from the 2nd element, which is index [1], and onward
for possible in studentScores[1:]: #starts from index 1 and goes to the end of the list
    if possible > highest: #here we compare each number with the current highest number, the latter defined as "highest"
        highest = possible #update highest number if a higher grade exists than the one defined as "highest"

print(f"The highest grade here is {highest}.") 

##---------------------##
print("\nEXERCISE 4")
print("Let's add all the numbers from 1 to 100! The best part, we don't have to write out 100 numbers to do that :)")
total = 0
for number in range(1, 101):
    total += number #adds each number in the range to the total, and loops through this until the upper limit (100) is reached)
print(f"The sum of all the numbers from 1 to 100 is {total}.")

##---------------------##
print("\nEXERCISE 5")
print("Now let's find the sum of all even numbers from 1 to some number X.")
while True:
    written = input("Write an integer between 0 and 1000, or write 'done' when finished: ")
    if written.lower() == "done":
        break #stops for loop
    try:
        written = int(written)
        if 0 <= written <= 1000: #number needs to be within range of 0 to 1000
            sumEven = 0 #if number is in range, then we consider initial sum to be zero in the beginning
            for something in range(2, written+1, 2): #adds 1 to the highest amount stored in "written" so that's included, 2 at the end means every other number
                sumEven += something #adds each input in written to the overall sumEven
            print(f"The sum of all even numbers from 1 to {written} is {sumEven}." )
        else:
            print("Invalid. Stay in the range.") #if you type a number outside the range, this pops up
    except ValueError:
        print("VERY invalid. Only integers or 'done', please.") #if you don't type an integer, this pops up

##---------------------##
print("\nEXERCISE 6")
print("Now let's figure out the solution to the Fizzbuzz game.")
#rules are:
#1) print numbers 1-100 (including 100)
#2) print Fizz INSTEAD of the number if the number is divisible by 3
#3) print Buzz INSTEAD of the number if the number is divisible by 5
#4) print FizzBuzz INSTEAD of the number if the number is divisible by 15 (i.e., 5*3)

for num in range(1, 101): 
    if num % 3 == 0 and num % 5 == 0: #if 3 and 5 are both divisors
        print("FizzBuzz")
    elif num % 3 == 0: #if just 3 is a divisor
        print("Fizz")
    elif num % 5 == 0: #if just 5 is a divisor
        print("Buzz")        
    else: #if neither 3 nor 5 are divisors
        print(num)

##---------------------##
print("\nEXERCISE 7")
print("Now let's make a password generator!\n")
import random

#lists we need for the characters that can be in the password
lala = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numnum = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to the PyPassword Generator!")
pwLetters = int(input("How many letters would you like in your password?\n"))
pwNumbers = int(input("How many numbers would you like?\n"))
pwSymbols = int(input("How many symbols would you like?\n"))

passwordList = [] #list of characters to be used in password

for character in range(1, pwLetters + 1):
    passwordList.append(random.choice(lala))

for character in range(1, pwNumbers + 1):
    passwordList.append(random.choice(numnum))

for character in range(1, pwSymbols + 1):
    passwordList.append(random.choice(symbols))

random.shuffle(passwordList) #shuffles the items in the list called "password"
password = "" #password is a string
for character in passwordList: #looks over the characters added to "passwordList"
    password += character #adds newly appended characters to the overall password
print(f"Your password is: {password}.")