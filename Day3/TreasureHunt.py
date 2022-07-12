print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input("🧙:Hello traveller, The tresaure you seeek is hard to find are you ready for the challeneg?(y/n)\n")
if choice == 'y' or choice == 'Y':
  print("Very well then. You shall follow this road and you will reach your destiniation.")
  print("You entered a vast jungle full of deadly animals.")
  jungle = input("You see a grizzly bear. What will you do? (run/play ddead)\n")
  if jungle == 'play dead':
    print("Clever! Bear is full and go past you.")
    river = input("You see a river. What will you do?(swim/wait)\n")
    if river == 'wait':
      print("You found a boat and cross the river.")
      path = input("You see two different paths? which one will you take? (left/right)\n")
      if path == 'right':
        print('You entered a cave.')
        cave = input("The cave has 3 rooms. Which one will you go?(1/2/3)\n")
        if cave == '2':
          print("🧙: Congratulations traveller! You found the treasure.")
        elif cave == '1':
          print("You entered the room on fire. You are dead.👽")
        else:
          print("You entered room full of beasts. You are dead. 👽")
      else:
        print("You fell into a trap. You are dead.👽")
    else:
      print("River is full of crocodiles.🐊 You are dead.👽")
  else:
    print("Bear saw you running and eat you. You are dead. 👽")
else:
  print("🧙: Well then traveller goodbye!")
