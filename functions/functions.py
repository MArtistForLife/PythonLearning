##---------------------##
print("EXERCISE 1")
def newFunction():
    print("Hi!")
    print("Life can be interesting if you keep exploring it :)")
newFunction() #defining the function isn't enough, you need to call it OUTSIDE the indented lines for it to return in the terminal

##---------------------##
print("\nEXERCISE 2")
print("For the game, robot starts at location (x,y) = (1,1) and must travel to position (13, 1).")
print("At this link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json")

#this is for Reeborg's World -- my notes are original, the code was partially written by me and then partially by LZ
# def moveRight(): #the robot has to turn left 3 times and THEN move in order to turn right
#     turn_left()
#     turn_left()
#     turn_left()
#     move()
# def moveNext(): #this is how the robot goes around the wall obstacles
#     move()
#     turn_left()
#     move()
#     turn_left()
#     turn_left()
#     turn_left()
#     move()
# def BoilerGo(num): #I DIDN'T COME UP WITH THIS FUNCTION TITLE...hahahaha
#     for i in range(num): #because the robot has to repeat those same movements a couple times to clear obstacles and get to the end
#         moveNext()
#         moveRight()
#         turn_left()
# BoilerGo(6) #yeah, somehow repeating those series of movements 6 times WORKED

##---------------------##
print("\nEXERCISE 3")
print("Here we go again.")
# def turnRight(): #using this again
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     while wall_on_right(): #the wall on your right is a reference to move...
#         move()
#     turnRight()
#     move()
#     turnRight()
#     while front_is_clear(): #but if there is a wall in front of you, wall_on_right() can't be the only reference
#         move()
#     turn_left()
   
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

##---------------------##
print("\nEXERCISE 4")
print("Last one: Reeborg and a maze.")
# def turnRight(): #this robot still doesn't know how to turn right without our help
#     turn_left()
#     turn_left()
#     turn_left()

# while not at_goal():
#     if right_is_clear(): #if there's no wall on the right, turn towards the right and walk
#         turnRight()
#         move()
#     elif front_is_clear(): #if there IS a wall on the right but nothing in front, just walk straight ahead
#         move()
#     else: #if there are walls on the right AND in front, turn left, then we can check again if the right and/or in front are clear yet
#         turn_left()