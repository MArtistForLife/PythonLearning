##---------------------##
print("EXERCISE 1")

programmingDict = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}
#this format is common: a new line for each entry and its definition

print(programmingDict["Bug"]) #this prints the value of the key "bug"
programmingDict["Loop"] = "The action of doing something over and over again." #adds a new word and definition
print(programmingDict) #prints the full dictionary

emptyDict = {}
programmingDict["Bug"] = "A moth in your computer" #changes the definition of a bug!!
print(programmingDict)

for key in programmingDict:
    print(key) #prints anything that is simply a word in the programming dictionary
    print(programmingDict[key])

##---------------------##
print("\nEXERCISE 2")

studentScores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

studentGrades = {} #this is an empty dictionary because it will be added to
for student in studentScores:
    score = studentScores[student] #the value of some student's score in the studentScores dictionary
    if score > 90:
        studentGrades[student] = "Outstanding!"
    elif score > 81 and score <= 90:
        studentGrades[student] = "Exceeds Expectations!"
    elif score > 71 and score <= 80:
        studentGrades[student] = "Acceptable"
    elif score <= 70:
        studentGrades[student] = "Fail"

print("The students and their grades, as determined by their preset scores, are as follows:")
print(studentGrades) #prints the now filled dictionary of students and their scores as graded

##---------------------##
print("\nEXERCISE 3")
print("Now we're going to make a travel log to which we can add new countries.")
country = input("Write the name of a country: ")
visits = int(input("Write the number of visits you have made to this country: "))
citiesList = input("Write the names of the cities in this country you have gone to: ")

#this next variable goes through the string of city names
#whether they are separated by spaces or commas, each city name will be SPLIT into a list of words based on whitespace
#the .strip() module removes whitespace from each city name, so each city name has no extra spaces around it
citiesCommas = [city.strip() for city in citiesList.replace(",", " ").split()]

#the travel log is a list of dictionaries #remember, BRACKETS for lists, and CURLY braces for dictionaries
travelLog = [
    {
        "country": "France", 
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany", 
        "visits": 5, 
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def addCountry(name, visitNumber, groupCities):
    newCountry = {} #dictionaries
    newCountry["country"] = name #for the "word" of each entry in the country dictionary
    newCountry["visits"] = visitNumber #for the "word" of each entry in the visits dictionary
    newCountry["cities"] = groupCities #for the "word" of each entry in the cities dictionary
    travelLog.append(newCountry) #adds the new country and its details to the list as a new dictionary in the list

addCountry(country, visits, citiesCommas) #use the inputs that WE have, not the generic ones defined in the addCountry function

if visits == 1:
    print(f"I've been to {travelLog[2]['country']} {travelLog[2]['visits']} time.")
else:
    print(f"I've been to {travelLog[2]['country']} {travelLog[2]['visits']} times.") #this will look at the 2nd entry and pull out country and visits

print(f"One cool city was {travelLog[2]['cities'][0]}.") #pulls out city name with index 0 from 2nd entry in travelLog

favorite = input("What was your favorite city? ")
print(f"My favorite city was {favorite}.")

##---------------------##
print("\nEXERCISE 4")
print("Now we're going to consider a silent auction scenario.")

bidders = {}
biddingGoing = True

def highestBidder(bidderExpense): #this is a generic parameter for highest bidder
    highestBid = 0 #start the highest bid at zero, like when the silent auction is just starting
    winner = "" #winner is intiially an empty string
    for bidder in bidderExpense:
        bidAmount = bidderExpense[bidder]
        if bidAmount > highestBid:
            highestBid = bidAmount
            winner = bidder
    print(f"The winner is {winner} with a bid of S{bidAmount}!")

print("\nWelcome to the secret auction program!.")

while biddingGoing:
    name = input("What is your name? ")
    price = int(input("What is your bid? S"))
    bidders[name] = price  #price (value) will be the value given the name (key) from the bidders dictionary
    maybeContinue = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if maybeContinue == "no":
        biddingGoing = False #if we don't need to continue, the bidding doesn't need to continue, either
        highestBidder(bidders) #call the name of the dictionary made earlier
    elif maybeContinue == "yes":
        bidders.clear() #removes all items from a list, dictionary, set, or other mutable collection; the collection now is an empty one
        #e.g., if you have [1,2,3,4], the clear() will leaves you with [] instead