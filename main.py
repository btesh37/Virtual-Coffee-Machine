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

MONEY = 0
resources["money"] = MONEY

# TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
def start_game():
    while True:
        global MONEY
        drink_choice = input("What would you like? (espresso/latte/cappuccino): ")

# TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt.

        def turn_off():
            if drink_choice == "off":
                quit();
        turn_off();

# TODO: 3. Print report

        def status():
            global MONEY
            for key in resources:
                print(key, resources[key])
            start_game();

        if drink_choice == "report":
            status();

# TODO: 4. Check resources sufficient?

        if drink_choice == "espresso":
            for i in resources:
                if i == "water":
                    if resources[i] < MENU["espresso"]["ingredients"]["water"]:
                        print("Sorry there is not enough water.")
                        start_game();
                elif i == "coffee":
                    if resources[i] < MENU["espresso"]["ingredients"]["coffee"]:
                        print("Sorry there is not enough coffee.")
                        start_game();
        elif drink_choice == "latte":
            for i in resources:
                if i == "water":
                    if resources[i] < MENU["latte"]["ingredients"]["water"]:
                        print("Sorry there is not enough water.")
                        start_game();
                elif i == "milk":
                    if resources[i] < MENU["latte"]["ingredients"]["milk"]:
                        print("Sorry there is not enough coffee.")
                        start_game();
                elif i == "coffee":
                    if resources[i] < MENU["latte"]["ingredients"]["coffee"]:
                        print("Sorry there is not enough coffee.")
                        start_game();
        elif drink_choice == "cappuccino":
            for i in resources:
                if i == "water":
                    if resources[i] < MENU["cappuccino"]["ingredients"]["water"]:
                        print("Sorry there is not enough water.")
                        start_game();
                elif i == "milk":
                    if resources[i] < MENU["cappuccino"]["ingredients"]["milk"]:
                        print("Sorry there is not enough coffee.")
                        start_game();
                elif i == "coffee":
                    if resources[i] < MENU["cappuccino"]["ingredients"]["coffee"]:
                        print("Sorry there is not enough coffee.")
                        start_game();

# TODO: Process coins

        print("Please insert coins.")

        quarters = int(input("how many quarters?: "))
        quarter_price = quarters * 0.25
        dimes = int(input("how many dimes?: "))
        dime_price = dimes * .10
        nickles = int(input("how many nickles?: "))
        nickle_price = nickles * .05
        pennies = int(input("how many pennies?: "))
        pennie_price = pennies * .01

        coins_inserted = (quarter_price + dime_price + nickle_price + pennie_price)

# TODO: Check transaction successful?

        if drink_choice == "espresso":
            if coins_inserted < MENU["espresso"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                start_game();
            elif coins_inserted == MENU["espresso"]["cost"]:
                resources["money"] += coins_inserted
            else:
                resources["money"] += MENU["espresso"]["cost"]
                change = coins_inserted - MENU["espresso"]["cost"]
                change = round(change, 2)
                print(f"Here is ${change} dollars in change.")
        elif drink_choice == "latte":
            if coins_inserted < MENU["latte"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                start_game();
            elif coins_inserted == MENU["latte"]["cost"]:
                resources["money"] += coins_inserted
            else:
                resources["money"] += MENU["latte"]["cost"]
                change = coins_inserted - MENU["latte"]["cost"]
                change = round(change, 2)
                print(f"Here is ${change} dollars in change.")
        elif drink_choice == "cappuccino":
            if coins_inserted < MENU["cappuccino"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                start_game();
            elif coins_inserted == MENU["cappuccino"]["cost"]:
                resources["money"] += coins_inserted
            else:
                resources["money"] += MENU["cappuccino"]["cost"]
                change = coins_inserted - MENU["cappuccino"]["cost"]
                change = round(change, 2)
                print(f"Here is ${change} dollars in change.")

# TODO: Make Coffee

        if drink_choice == "espresso":
            if coins_inserted == MENU["espresso"]["cost"] or coins_inserted > MENU["espresso"]["cost"]:
                water_remaining = resources["water"] - MENU["espresso"]["ingredients"]["water"]
                resources["water"] = water_remaining
                coffee_remaining = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
                resources["coffee"] = coffee_remaining
                print(f"Here is your {drink_choice} ☕️. Enjoy!")
        elif drink_choice == "latte":
            if coins_inserted == MENU["latte"]["cost"] or coins_inserted > MENU["latte"]["cost"]:
                water_remaining = resources["water"] - MENU["latte"]["ingredients"]["water"]
                resources["water"] = water_remaining
                coffee_remaining = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
                resources["coffee"] = coffee_remaining
                milk_remaining = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
                resources["milk"] = milk_remaining
                print(f"Here is your {drink_choice} ☕. Enjoy!")
        elif drink_choice == "cappuccino":
            if coins_inserted == MENU["cappuccino"]["cost"] or coins_inserted > MENU["cappuccino"]["cost"]:
                water_remaining = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
                resources["water"] = water_remaining
                coffee_remaining = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
                resources["coffee"] = coffee_remaining
                milk_remaining = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
                resources["milk"] = milk_remaining
                print(f"Here is your {drink_choice} ☕. Enjoy!")

start_game();

