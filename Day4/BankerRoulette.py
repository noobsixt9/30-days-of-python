import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(",")

name_num = len(names)
random_int = random.randint(0, name_num-1)
name_to_pay = names[random_int]
print(name_to_pay,"is going to buy the meal today!")

