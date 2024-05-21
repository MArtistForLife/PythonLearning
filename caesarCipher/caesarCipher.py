##---------------------##
print("EXERCISE 1")

def greet(name): #name is now a input of this function called greet
    print(f"Hello there, {name}")
    print(f"What an interesting thing, to be communicating with your computer or device, huh, {name}?")
    print("Maybe you were sleeping or watching videos on YouTube or Xiaohongshu.")

greet("Maia") #define the input, which in this case is the name

print("")
def greeting(name, location): #function has 2 inputs
    print(f"Hello, {name}!")
    print(f"Welcome to {location}!")

greeting("Maia", "West Lafayette")

print("")
def newGreet(name = "Maia", location = "Purdue campus"):
    print(f"How is {location} like, {name}?")

newGreet()

##---------------------##
print("\nEXERCISE 2")
print("Imagine you're painting a wall. Given the height and width of wall, let's calculate how many paint cans you need.")
import math

def wallPainting(height, width, coverage): #3 inputs that are relevant here: height, width, and coverage
    cansNeeded = math.ceil((height * width) / coverage) #ceil is short for ceiling, so basically this will always round up (helpful if we have something like 2.3 or 4.1)
    print(f"The height is {height} meters and the width is {width} meters, so you need {cansNeeded} cans.")

wallPainting(2, 4, 5)
wallPainting(4, 5, 5)
wallPainting(3, 9, 5)

##---------------------##
print("\nEXERCISE 3")
print("Now let's consider whether a number is a prime number or not.")

def numberStatus(number):
    if number < 2: #checks first if the number is less than 2; if so, we go through this if statement's conditions
        prime = False
        print(f"{number} is not a prime number.")
        return #exits the function and returns the value back, so if all three of these conditions are met, we don't need to go further
    prime = True #otherwise, the number is assumed initially to be prime
    for divisor in range(2, number): #given that the number is greater than or equal to 2, we now consider the for loop conditions
        if number % divisor == 0: #if any values between 2 and the number can divide evenly into the number, then it isn't prime
            prime = False
            break #stop the function altogether
    if prime: #if after the above checks (number is greater than or equal to 2, and the divisor check has been made)
        print(f"{number} is a prime number.")
    else: #i.e., if some values do NOT divide evenly into the number
        print(f"{number} is not a prime number.")

numberStatus(0) #calling the function to test first if conditional
numberStatus(19) #calling again to test the for loop

##---------------------##
print("\nEXERCISE 4")
print("Now we're going to try out a Caesar cipher.")

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(writtenText, shiftAmt):
#     cipherMessage = ""
#     for letter in writtenText: #for some letter in the text (the word to be encrypted)
#         if letter in alphabet:
#             position = alphabet.index(letter) #goes into the alphabet list and determines the position of this letter in that list
#             newPosition = position + shiftAmt #takes the shift number and moves the letter's original index in the alphabet by that shift number
#             newLetters = alphabet[newPosition] #looks at the new position in the alphabet and pulls out THAT new letter for the encryption
#             cipherMessage += newLetters #accumulates these new ciphered letters to make the letters of the cipher
#         else:
#             cipherMessage += letter #characters not in the alphabet are kept the same
#     print(f"The encoded message is: {cipherMessage}")

# def decrypt(cipherMessage, shiftAmt):
#     realMessage = ""
#     for letter in cipherMessage: #for some letter in the cipher message (which will be decrypted)
#         if letter in alphabet:
#             position = alphabet.index(letter) #goes into the alphabet list and determines the position of this letter in that list
#             realPosition = position - shiftAmt #takes the shift number and moves the letter's shifted index in the alphabet back to its original by that shift number
#             realLetters = alphabet[realPosition] #looks at the real position in the alphabet and pulls out THAT letter for the decryption
#             realMessage += realLetters #accumulates those "real letters" to make the real message
#         else:
#             realMessage += letter #once again, characters not in the alphabet remain the same
#     print(f"The decoded message is : {realMessage}")
    
# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)

#below is a more concise version of the above code that is commented out
def caesar(givenText, shiftAmt, wayToGo):
    finishedText = ""
    if wayToGo == "decode":
        shiftAmt *= -1 #take the shift amount and multiply it by -1 to move the letter indices back that much for DEcoding
    for letter in givenText: #for any letter that is in the message given (whether or not it needs to be encoded or decoded)
        if letter in alphabet:
            position = alphabet.index(letter) #goes into the alphabet list and determines the position of some letter in that list
            newPosition = (position + shiftAmt) % 26 #takes the shift number and moves the letter's original index in the alphabet by that shift number
            finishedText += alphabet[newPosition] #looks at the new position in the alphabet and pulls out THAT new letter for the encryption
        else:
            finishedText += letter #keeps characters not in the alphabet kept the same
    print(f"The {wayToGo}d message is: {finishedText}")
#the above is only DEFINING a function -- we haven't called it yet

goMore = True
while goMore:
    direction = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower() #makes the message all lowercase
    shift = int(input("Type the shift number:\n"))

    #what if the shift given is LARGER than the number of items (letters) in the alphabet list??
    shift = shift % 26 #gives the remainder of whatever the quotient contains, that way if some big number is given we only get remainder
    caesar(text, shift, direction)
    again = input("Do you want to use the cipher again? Type 'yes' or 'no':\n")
    if again == "no":
        goMore = False
        print("Alright, then! Bye for now :)")