##---------------------##
print("EXERCISE 1")
print("Now let's play a game of Hangman!")
#this below is NOT code to be run; just trying to structure a rough flow of how the rules in hangman go
# if start:
#     generateRandomWord()
#     word = []
#     generateBlanks() #generate as many blanks as letters in the word
#     letterGuess = input("Guess a letter: ")
#     if letterGuess in word: #if the letter guessed IS in the word
#         replaceBlank() #replace blank with the letter in correct spot
#         if blanksFilled: #if all the blanks are filled
#             print("Game Over")
#         else: #if the blanks aren't all filled
#             letterGuess = input("Guess another letter: ")
#     else: #if the letter guessed isn't in the word
#         loseLife() #lose a life
#         if livesGone: #if you ran out of lives
#             print("Game Over")
#         else: #if you still have lives, guess another letter
#             letterGuess = input("Guess another letter: ") 

import random
wordList = ["aardvark", "baboon", "camel", "elephant", "flamingo", "giraffe", "hippopotamus", "iguana", "jaguar", "kangaroo",
    "lemur", "mongoose", "narwhal", "octopus", "penguin", "quokka", "rhinoceros", "salamander", "tortoise", "umbrella",
    "vulture", "walrus", "xenopus", "yak", "zebra", "alligator", "buffalo", "chameleon", "dolphin", "echidna", "falcon",
    "gazelle", "hamster", "ibex", "jellyfish", "koala", "lobster", "meerkat", "newt", "ostrich", "porcupine", "quail",
    "raccoon", "seahorse", "toucan", "urchin", "viper", "wombat", "xerus", "yellowfin", "zebu", "albatross", "bison",
    "chimpanzee", "dingo", "eagle", "flounder", "gecko", "heron", "impala", "javelina", "kiwi", "lemur", "manatee",
    "narwhal", "orca", "panther", "quoll", "reindeer", "squirrel", "tiger", "uakari", "viper", "wolverine", "xenarthra",
    "yak", "zebu", "antelope", "butterfly", "cricket", "dragonfly", "elephant", "frog", "gorilla", "hedgehog", "ibis",
    "jaguar", "kangaroo", "lemur", "manta", "newt", "octopus", "platypus", "quokka", "rabbit", "salmon", "turtle",
    "unicorn", "vulture", "whale", "xerus", "yak", "zebra", "armadillo", "beetle", "catfish", "dolphin", "eel", "flamingo",
    "giraffe", "hummingbird", "iguana", "jackal", "koala", "lion", "monkey", "numbat", "owl", "parrot", "quail", "rattlesnake",
    "seal", "toucan", "urchin", "vulture", "weasel", "xenops", "yak", "zebu", "anaconda", "bullfrog", "chinchilla", "dormouse",
    "elephant", "fox", "goose", "hawk", "iguana", "jaguar", "kangaroo", "lemur", "moose", "nightingale", "otter", "panda",
    "quagga", "rooster", "shark", "tarantula", "urial", "vole", "wolf", "xiphias", "yellowhammer", "zebra"]
chosenWord = random.choice(wordList) #randomly chooses word from list and assigns it to variable called "chosenWord"
#print(f"The solution is {chosenWord}.")

display = ["_" for _ in chosenWord] #blanks are gonna be displayed
lives = 6 #head, left arm, right arm, body, left leg, right leg makes 6 chances total

def hangmanPicture(lives):
    if lives == 5:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |")
        print(" |")
        print("_|_")
    elif lives == 4:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |       |")
        print(" |")
        print("_|_")
    elif lives == 3:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |      /|")
        print(" |")
        print("_|_")
    elif lives == 2:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |      /|\\")
        print(" |")
        print("_|_")
    elif lives == 1:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |      /|\\")
        print(" |      /")
        print("_|_")
    elif lives == 0:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |      /|\\")
        print(" |      / \\")
        print("_|_")        

while "_" in display and lives > 0: #while there are still blanks in the display
    letterGuess = input("\nGuess a letter: ").lower() #prompts user to guess a letter and then makes that letter lowercase

    if letterGuess in display:
        print("Wait! You already guessed that letter. Guess another one.")
        continue

    if letterGuess in chosenWord: #if the letter guessed is one in the chosen word...
        for index, letter in enumerate(chosenWord): #for whatever letter is at the indices in the chosen word (enumerate returns those 2 parameters)
            if letter == letterGuess:
                display[index] = letterGuess #changes the blank space at that index to the guessed letter if correct
        print("Great job, that letter's in there!")
    else: #if the letter guessed is NOT one in the chosen word
        lives -= 1
        if lives > 1:
            print(f"Yikes, that letter isn't in the word. You got {lives} lives left.")
        elif lives == 1:
            print(f"Yikes, that letter isn't in the word. You got {lives} life left.")
        hangmanPicture(lives) #draw hangman picture based on remaining lives
    
    print(" ".join(display)) #join is a method that concatenates elements of iterables (e.g., list) into ONE string, so it won't be returned as a list of elements in the terminal

if "_" not in display:  #if there are no more blank spaces
    print(f"Yay! You've guessed the word: {chosenWord}")
else: #if there are still blank spaces left but you ran out of lives
    print(f"Sorry, you ran out of lives. The word was: {chosenWord}")