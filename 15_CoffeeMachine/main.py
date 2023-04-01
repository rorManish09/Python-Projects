

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 1Print the report of all coffee machine resource

for items, quantity in resources.items():
    print(items, ':', quantity)


# TODO: 2 Check the resources are sufficient to make a drink or not
for items, quantity in resources.items():
    if items == 'milk' and resources[items] < 100 or items == 'water' and resources[items] < 50 or items== 'coffee' and resources[items]<18:
        print(f"Insufficient: {items} Quantity:{resources[items]} ")
    else:
        print(f"Sufficient: {items} Quantity: {resources[items]} ")








