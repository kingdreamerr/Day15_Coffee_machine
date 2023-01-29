coffees = ["espresso", "late", "cappuccino", "off"]
# recipes =
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

in_use = True


def enough_resources(coffee):
    for d_items in coffee:
        if coffee[d_items] >= resources[d_items]:
            print(f"Sorry there is not enough {d_items}")
            return False
    return True


while in_use:

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        in_use = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")
    else:
        drink = MENU[choice]
        enough_resources(drink['ingredients'])
    #
    # is_choice_correct = False
    #
    # while choice != "off" and choice != "report" and choice not in coffees:
    #     if choice not in coffees:
    #         print("please enter a valid option")
    #         choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    #     else:
    #         is_choice_correct = True
    #
    # if choice == "off":
    #     in_use = False
    #
    # elif choice == "report":
    #     report(resources)
    #
    # if choice in coffees:
    #     print("Please insert coins.")
    #     quarters = int(input("How many quarters?: "))
    #     dimes = int(input("How many dimes?: "))
    #     quarters = int(input("How many quarters?: "))
    #     quarters = int(input("How many quarters?: "))
    #
