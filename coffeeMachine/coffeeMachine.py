##---------------------##
print("EXERCISE 1")
print("Now we're going to look at a digital version of a coffee machine.")

############ criteria for coffee machine ############
#make 3 hot flavors (espresso, latte, cappuccino)
#espresso - 50 mL water and 18 g coffee ($1.50)
#latte - 200 mL water, 24 g coffee, and 150 mL milk ($2.50)
#cappuccino - 250 mL water, 24 g coffee, and 100 mL milk ($3)

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

off = False

#FUNCTION to get drink cost
def checkDrinkCost(drinkName):
    if drinkName in MENU: #for any drink listed in MENU dictionary
        return MENU[drinkName]["cost"] #returns the cost of the drink
    else:
        return "This drink isn't on the menu."

#FUNCTION to check if resources sufficient
def checkResources():
    #return resources this works, but it only returns the dictionary in 1 line
    for ingredient, amount in resources.items():
        print(f"{ingredient}: {amount}")
    
#FUNCTION to process coins
def processCoins(drinkPrice):
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickles = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    customerPayment = quarters + dimes + nickles + pennies
    
    difference = round(drinkPrice - customerPayment, 2)

    if customerPayment > drinkPrice:
        customerChange = abs(difference)
        print(f"Here is ${customerChange:.2f} in change.") #gives the customer change to 2 decimal places
        return True #payment is successful
    elif customerPayment < drinkPrice:
        shortBy = abs(round(difference, 2))
        print(f"Whoops, that's not enough. You're short by ${shortBy:.2f}, so you're refunded.")
        return False

#FUNCTION to check if making drink is feasible given current resources
def canWeMakeDrink(drinkName):
    ingredients = MENU[drinkName]["ingredients"]

    #fr the below, ingredient SINGULAR is an element in the dictionary CALLED ingredients PLURAL
    for ingredient, neededAmt in ingredients.items(): #considers the items listed under "ingredients" in the bigger dictionary
        if ingredient not in resources:
            return False, f"{ingredient} isn't available."
        if resources[ingredient] < neededAmt: #looks at ingredient amt in resources
            return False, f"There isn't enough {ingredient}. We need {neededAmt} and there is only {resources[ingredient]}."
            #resources[ingredient] accesses the amount of a specific ingredient in the resources dictionary

    return True, None #if all ingredients are available in the quantities needed
    #None indicates that there is no error message from this

#FUNCTION for making drink
def makeDrink(drinkName):
    ingredients = MENU[drinkName]["ingredients"]
    for ingredient, neededAmt in ingredients.items():
        resources[ingredient] -= neededAmt
    print(f"Here is your {drinkName}. Enjoy!")

while True:
    drinkName = input("What would you like? (espresso, latte, cappuccino, OR 'report' for update on inventory): ").lower()

    if drinkName in MENU: #if the given drink name is something in the menu dictionary
        drinkPrice = checkDrinkCost(drinkName) #runs the function to check cost of given drink
        print(f"One {drinkName} costs ${drinkPrice:.2f}.")
    
        canMake, message = canWeMakeDrink(drinkName)
        if not canMake:
            print(message) #will print None for the message and True for canMake if everything is good to go
            continue

        if processCoins(drinkPrice):
            makeDrink(drinkName)
        else:
            print("Fail on payment! Try again :( ")

    elif drinkName == "report":
        checkResources() #print report
    elif drinkName == "off":
        print("Okay, turning off coffee machine.")
        break
    else:
        print("Invalid response! Try again. ")




        


