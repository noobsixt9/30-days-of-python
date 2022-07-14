rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random 
game_images = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(game_images[user])
computer = random.randint(0, 2)
print(game_images[computer])
if computer == user:
  print("It's a draw")
elif computer > user:
  print("Computer Wins")
elif user > computer:
  print("You win")
elif user == 0 and computer == 2:
  print("You win")
elif user == 2 and computer == 0:
  print("Computer wins")
elif user >=3 or user < 0:
  print("You entered invalid number. You lose")
