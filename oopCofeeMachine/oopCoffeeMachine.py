##---------------------##
print("EXERCISE 1")
print("Now we're going to use a version of the coffee machine that is OOP.")

############ criteria for OOP version ############
# classes are MenuItem, Menu, CoffeeMaker, MoneyMachine
# MenuItem has 3 attributes: name (str), cost (float), and ingredients (dictionary)
# Menu has 2 methods: getItems() and findDrink(orderName)
# CofeeMaker has 3 methods: report(), isResourcesSufficient(drink), and makeCoffee(order)
# MoneyMachine has 3 methods: report(), processCoins(), makePayment(cost)

############ criteria for OOP version ############
# classes are MenuItem, Menu, CoffeeMaker, MoneyMachine
# MenuItem has 3 attributes: name (str), cost (float), and ingredients (dictionary)
# Menu has 2 methods: getItems() and findDrink(orderName)
# CoffeeMaker has 3 methods: report(), isResourcesSufficient(drink), and makeCoffee(order)
# MoneyMachine has 3 methods: report(), processCoins(), makePayment(cost)

class MenuItem:
    def __init__(self, name, cost, ingredients): #init is used to initialize the attributes
        self.name = name
        self.cost = cost
        self.ingredients = ingredients     
        
espresso = MenuItem("espresso", 1.50, {"water": 50, "coffee": 18})
latte = MenuItem("latte", 2.50, {"water": 200, "milk": 150, "coffee": 24})
cappuccino = MenuItem("cappuccino", 3.00, {"water": 250, "milk": 100, "coffee": 24})

class Menu:
    def __init__(self):
        self.MenuItem = [espresso, latte, cappuccino]
    
    def getDrink(self):
        return [drink.name for drink in self.MenuItem]
    
    def findDrink(self, orderName):
        for item in self.MenuItem:
            if item.name == orderName:
                return item
        return None #if not
    
class CoffeeMaker:
    def __init__(self):
        self.resources = {"water": 300, "milk": 200, "coffee": 100}

    def report(self):
        for resource, amount in self.resources.items():
            if resource == "water" or resource == "milk":
                print(f"{resource.capitalize()}: {amount} mL") #to check the quantity of stuff
            elif resource == "coffee":
                print(f"{resource.capitalize()}: {amount} g")

    def isResourcesSufficient(self, drink):
        for ingredient, amount in drink.ingredients.items():
            if amount > self.resources.get(ingredient, 0):
                print(f"Sorry, there's not enough {ingredient}.")
                return False
            return True #otherwise, if the amount needed is less than what we still have
    
    def makeCoffee(self, order):
        for ingredient, amount in order.ingredients.items():
            self.resources[ingredient] -= amount
        print(f"Here is your {order.name}. Enjoy!")

class MoneyMaker:
    def __init__(self):
        self.profit = 0.0
    
    def report(self):
        print(f"Money: ${self.profit:.2f}")

    def processCoins(self):
        print("Please insert coins.")
        try:
            quarters = int(input("How many quarters? ")) * 0.25
            dimes = int(input("How many dimes? ")) * 0.10
            nickles = int(input("How many nickels? ")) * 0.05
            pennies = int(input("How many pennies? ")) * 0.01
        except ValueError: #to account for invaid inputs
            print("That's invalid! Please enter only whole numbers!")
            return 0.0
    
        customerPayment = quarters + dimes + nickles + pennies
        return customerPayment
    
    def makePayment(self, cost):
        payment = self.processCoins()
        if payment >= cost:
            change = round(payment - cost, 2)
            if change > 0:
                print(f"Here is ${change:.2f} in change!")
            self.profit += cost
            return True
        else: #if the payment given is not enough for the drink's cost
            print(f"Sorry, that's not enough money. You get a refund!")
            return False

offers = Menu()
machine = CoffeeMaker()
counter = MoneyMaker()

switchOn = True
while switchOn:
    options = ", ".join(offers.getDrink())
    choice = input(f"What would you like? ({options}): ")

    if choice == "off":
        switchOn = False
    elif choice == "report":
        machine.report()
        counter.report()
    else:
        drink = offers.findDrink(choice)
        if drink:
            print(f"The price of {drink.name} is ${drink.cost:.2f}.")
            if machine.isResourcesSufficient(drink) and counter.makePayment(drink.cost):
                machine.makeCoffee(drink)
