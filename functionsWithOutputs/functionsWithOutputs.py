##---------------------##
print("EXERCISE 1")

def formatName(fName, lName):
    """Write a first and last name and format it
    to return the title case version of the name."""
    #this makes the code more readable across multiple lines of across one really long one
    #interpreted as a COMMENT!!

    if fName == "" or lName == "":
        return "You didn't provide valid inputs."
    fixedFirst = fName.title() #title() makes all words capitalized (first letter uppercase, others lowercase)
    fixedLast = lName.title() #does the same to the last name
    return f"The name is {fixedLast}. {fixedFirst} {fixedLast}." #just returns a value, different from print function

#print(f"The name is {fixedLast}. {fixedFirst} {fixedLast}.")

formatName("maIA", "TALBERT") #this calls the function and fixes the name!
output = len("Maia")
print(f"The length of the name Maia is {output}.")

print(formatName(input("What is your first name? "),
    input("What is your last name? ")))

##---------------------##
print("\nEXERCISE 2")
print("Now we're going to convert the Leap Year function to one that finds the number of days in a month.")

#this is the leap year deal, adapted from the manage code in lesson 3 to be a function
def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            elif year % 400 != 0:
                return False
        elif year % 100 != 0:
            return True

def daysInMonth(year, month):
    monthsByDays = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month == 2 and isLeapYear(year):
        return 29
    else:
        return monthsByDays[month-1] #say if you want December (month 12), that is in index 11, so month - 1

year = int(input("Type a year: "))
month = int(input("Type a month by its number (e.g., 2 for February, 4 for April, etc.): "))
days = daysInMonth(year, month)
print(f"The number of days in month {month} of {year} is {days}.")

##---------------------##
print("\nEXERCISE 3")
print("Now we're going to use a calculator!")

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("Type a number: "))

    #to print out the symbols
    for symbol in operations: #it will list +, -, *, /, each on a separate line
        print(symbol)

    shouldContinue = True
    while shouldContinue:
        symbolToUse = input("Pick an operation from the lines above and type a symbol: ")
        num2 = float(input("Type another number: "))
        calculateFunction = operations[symbolToUse] #based on a symbol inputted, this variable called calculateFunction will tell us what operation is involved
        answer = calculateFunction(num1,num2) #and from that we can figure out what to do with our numbers!

        print(f"{num1} {symbolToUse} {num2} = {answer}") #prints the equation!

        if input(f"Type 'yes' to continue calculating with {answer}, or 'no' to start over: ") == "yes":
            num1 = answer
        else:
            shouldContinue = False
            calculator() #this is a little detail that prevents something like an infinite loop and also makes the function call recursive
            #also keeps the calculator function organized

calculator() #calling the function
# symbolToUse = input("Pick an operation from the lines above and type a symbol: ")
# num3 = int(input("Let's go! Type another integer: "))
# calculateFunction = operations[symbolToUse] #based on a symbol inputted, this variable called calculateFunction will tell us what operation is involved
# anotherAns = calculateFunction(answer,num3) #and from that we can figure out what to do with our numbers!
# print(f"{answer} {symbolToUse} {num3} = {anotherAns}")