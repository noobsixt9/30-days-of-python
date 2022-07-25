from promise import promise_for_dict
from data import resources,MENU
profit = 0
def check_resources(ordered_item):
    """check if resources are enough to make coffe"""
    for item in ordered_item:
        if ordered_item[item] > resources[item]:
            print(f"sorry, There is not enough {item}")
            return False
        return True

def process_coins():
    """recieves payment"""
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many penny?: ")) * 0.01
    return total

def is_payment_done(pay,order_cost):
    """check if payment is done or not"""
    if pay >= order_cost:
        global profit
        profit += order_cost
        change = round(pay - order_cost, 2)
        print(f"Here is your change ${change}.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """makes coffee and reduce amount of ingredients used to make coffe from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} coffe.")

is_machine_on = True
while is_machine_on:
    choice = input("What would you like?(espresso/latte/cappuccino): ")
    if choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Milk: {resources['milk']}")
        print(f"profit: ${round(profit, 2)}")
    elif choice == "off":
        is_machine_on = False
    else:
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
            print("Please insert coins")
            payment = process_coins()
            if is_payment_done(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
        
            


