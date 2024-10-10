#------example1------#

def shortFunction(x):
    return x*2
#we could call this by its name with a number (not x) to get value returned

equivAnony = lambda x: x*2 #lambda = for all the (blah blah blah) parameters
#this performs the same task as shortFunction
#we can just define our variable and then what to do to that variable
#so, it is anonymous bc we don't need to name 
#doesn't require a name unless assigned to a varibale like equivAnony
#LESS TYPING YAHOO

#------example2------#

def applyToList(someList, f):
    return [f(x) for x in someList]
#lengthy as hell, so let's use lambda

ints=[4,0,1,5,6]
applyToList(ints, lambda x: x*2)
#lambda method of defining variable and then operation = SIMPLER

###CURRYING--making new functions from existing ones by partial argument application

#------example3------#

#our trivial function
def addNumbers(x,y):
    return x+y #take 2 simple variables, x and y, and return their sum

#our new function
addFive = lambda y: addNumbers(5, y)
#adds 5 to the argument
#the first argument is fixed at 5...
#so, the second argument y gets passed when you call addFive(y)
#example of how it works: addFive(3) will behave like you called addNumbers(5,3), so you get 8
#because you get 5 added to whatever value you provide for the second argument y

#our 2nd new function (the one that gets curried)
#because all we do is make a new function that CALLS an existing function
from functools import partial
addFive = partial(addNumbers, 5)
#we take a function that usually needs MULTIPLE arguments
#and instead make a new function with some of those arguments already "pre-filled"
#here, first argument is fixed at 5 in addNumbers
#so this functions like lambda, but is more explicit and reusable

#------example4------#

#instead of this...
someDict = {'a': 1, 'b': 2, 'c': 3}
for key in someDict:
    print(key)
#just gives you a, b, c in separate lines

dictIterator = iter(someDict)
# this would give you ['a', 'b', 'c']
#because for the dictionary, you get an iterator (object that helps you go through the list or dictionary 1 element at a time)
#so, you can go through the ditionary one key at a time, one by one

###GENERATOR = a concise way to construct a new iterable object
#(it returns a sequence of multiple results, pausing after each until the next one is requested)

###GENERATOR EXPRESSION = even more concise way to make a generator
#we get to use parentheses instead of brackets!!

sum(x**2 for x in range(100))