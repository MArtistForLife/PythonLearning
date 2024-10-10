##---------------------##
print("EXERCISE 1")
print("Now we're going to make our own class.")

#Pascal Case = first letter of every word in the class name is capitalized
## e.g., BasicClass
#Camel Case = first word in the class name is lowercase, everything after is capitalized
## e.g., basicClass
#Snake Case = all words in the class name are lowercase, separated by underscores
## e.g., basic_class

##below is more risky for inaccurate or inconsistent values
# user1 = User() #we use () because User is the name of the class
# user1.id = "925"
# user1.username = "maia"
# print(user1.username)

# user2 = User()
# user2.id = "506"
# user2.username = "lijun"
# print(user2.username)

# class Car:
#     def __init__(self): #initialize attributes
#        self.seats = seats

class User: #this is us making our own class
    #pass #this is used to define empty class or function
    def __init__(self, userID, username): #this is a constructor; it initializes attributes when the object is created
        print("new user being created...")
        self.id = userID #use dot notation to add attributes to an object
        self.username = username #we can keep doing this attribute-adding with dot notation
        self.followers = 0 #default values can be set here
        self.following = 0
        #constructors are automatically called when a new object is made
        #special method to initialize attributes when object is made

    def follow(self, user): #method named "follow," it takes another "User" object as an argument
        user.followers += 1 #increases followers of user who is BEING followed by 1
        self.following += 1 #increases followers of user who IS FOLLOWING by 1


user1 = User("925", "Maia") #define an object from a class using that class's name followed by parentheses
print(user1.username) #output is 0; access and print the attribute using dot notation
print(user1.followers) #output is 0
#less inefficiency and errors
#attributes' default values give flexibility
#using the init method ensures better ability to initialize the objects (give them starting values)

user2 = User("506", "Lijun")
# user2.id = "506"
# user2.username = "Lijun"
print(user2.followers)

print("looking at followers and following")
user1.follow(user2) #this means user1 will follow user2
print(user1.followers) #still 0 because user1 follows user2
#also, user1's followers don't change, only the followING does
#the follow method is designed to increase the followers count of the user being followed, not the one who is following
#so the follow method makes user2 followers go up, NOT user1's followers
print(user1.following)
#since user1 is following user2, user1's followING count is incremented by 1

print(user2.followers) #since user1 is following user2, user2's followERS count goes up by 1
print(user2.following) #since user1 is following user2, user2 isn't following anyone, so user2 followING has not gone up

##---------------------##
print("EXERCISE 2")
print("Now we're going to make our the question class.")

class Question:

    def __init__(self, qText, qAnswer ):
        self.text
        self.answer

newQ = Question("sdfsdf", "False")
newQ.text

from data 