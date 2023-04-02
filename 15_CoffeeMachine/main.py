MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def  isResourceSufficient(order_ingerdient):

    """Returns True when order can be made, False ingerdents are insufficient """
    for item in order_ingerdient:
        if order_ingerdient[item] >= resources[item]:
            print(f"Sorry the is not enough {item}")
            return False
        return True


def process_coins():
    """Returns the Total calculated from coin inserted"""
    print("Please enter coins.")
    Total = int(input("How many Quarters ?")) * 0.25
    Total += int(input("How many Dime ?")) * 0.1
    Total += int(input("How many Nickels ?")) * 0.05
    Total += int(input("How many Penies ?")) * 0.01
    return Total


def Transaction(money_recieved, drinking_cost):
    """Return True when the  payment is accepted  or False if the money is  insufficient"""
    if money_recieved >= drinking_cost:
        change = round(money_recieved - drinking_cost, 2)
        print(f"Here is ${change} in change")
        global money
        money += drinking_cost
        return True
    else:
        print("Insufficient amount money is refunded.")
        return False


def make_coffe(drink_name, order_ingerdient):
    """Deduct the  required INgredient from the resources."""
    for item in order_ingerdient:
        resources[item] -= order_ingerdient[item]
    print(f"Here is your {drink_name}")


is_on = True

while is_on:

    userChoice = input('What would you like? (espresso/latte/cappuccino)').lower()

    if userChoice == 'off':
        is_on = False
    elif userChoice == 'report':
        for item, values in resources.items():
            print(item, ':', values)
        print(f"Money = $ {money}")

    else:
        drink = MENU[userChoice]
        if isResourceSufficient(drink["ingredients"]):
            payment = process_coins()
            if Transaction(payment, drink["cost"]):
                make_coffe(userChoice, drink["ingredients"])
