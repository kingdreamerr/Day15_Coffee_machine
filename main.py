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


def get_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_payment_successful(money_paid, drink_cost):
    if money_paid >= drink_cost:
        global profit
        profit += drink_cost
        difference = money_paid - drink_cost
        print(f"Here is ${round(difference,2)} dollars in change")
        return True
    else:
        print("Sorry that is not enough money")
        return False


def make_coffee(drink_name, order_ingredients):
    """Remove the required resources"""
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here is your {drink_name} enjoy!")


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
        if enough_resources(drink['ingredients']):
            payment = get_coins()
            if is_payment_successful(payment, drink["cost"]):
                make_coffee(choice, drink['ingredients'])

