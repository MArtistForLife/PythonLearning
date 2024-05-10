print("EXERCISE 1:")
num1=int(input("write a number: "))
num2=int(input("write another number: "))
print("the sum of these two numbers is " + str(num1+num2))

print("EXERCISE 2")
name = input("What is your name? ") #prompt for name
length = len(name) #returns number of items (characters) in name
print("the number of characters in this name is " + str(length)) #returns the result of len function for name in terminal

print("EXERCISE 3")
a=input("define a number: ")
b=input("define another number: ")
print("a: " + a)
print("b: " + b)

print("EXERCISE 4")
print("Welcome to the Band Name Generator.")
cityName = str(input("What's the name of the city you grew up in?\n"))
petName = str(input("What's your pet's name?\n"))
print("Your band name could be " + cityName + " " + petName + ".")   
