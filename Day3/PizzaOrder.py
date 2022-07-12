print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepper_small = 2
pepper_large = 3
cheese_extra = 1
if size == 'S':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            print(f"Your final bill is: ${small_pizza+pepper_small+cheese_extra}.")
        else:
            print(f"your final bill is: ${small_pizza+pepper_small}.")
    elif add_pepperoni == 'N' and extra_cheese == 'Y':
        print(f"your final bill is: ${small_pizza+cheese_extra}.")
    elif add_pepperoni == 'N' and extra_cheese == 'N':
        print(f"your final bill is: ${small_pizza}.")
if size == 'M':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            print(f"your final bill is: ${medium_pizza+pepper_large+cheese_extra}.")
        else:
            print(f"your final bill is: ${medium_pizza+pepper_large}.")
    elif add_pepperoni == 'N' and extra_cheese == 'Y':
        print(f"your final bill is: ${medium_pizza+cheese_extra}.")
    elif add_pepperoni == 'N' and extra_cheese == 'N':
        print(f"your final bill is: ${medium_pizza}.")
if size == 'L':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            print(f"your final bill is: ${large_pizza+pepper_large+cheese_extra}.")
        else:
            print(f"your final bill is: ${large_pizza+pepper_large}.")
    elif add_pepperoni == 'N' and extra_cheese == 'Y':
        print(f"your final bill is: ${large_pizza+cheese_extra}.")
    elif add_pepperoni == 'N' and extra_cheese == 'N':
        print(f"Your final bill is: ${large_pizza}.")
