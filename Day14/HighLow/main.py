import random 
from replit import clear
from art import logo,vs
from game_data import data

def random_user():
  return random.choice(data)

def format_output(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description} from {country}."

def check_answer(guess, a_follower, b_follwer):
  if a_follower > b_follwer:
    return guess == "a"
  else:
    return guess == "b"
def game():
  print(logo)
  score = 0
  a_account = random_user()
  b_account = random_user()
  should_cont = True

  while should_cont:
    a_account = b_account
    b_account = random_user()
    while a_account == b_account:
      b_account = random_user()
      
    print(f"Compare A: {format_output(a_account)}")
    print(vs)
    print(f"Against B: {format_output(b_account)}")
    guess = input("Who has more follower? Type 'A' or 'B': ").lower()
  
    a_follower_count = a_account["follower_count"]
    b_follower_count = b_account["follower_count"]
    is_true = check_answer(guess, a_follower_count, b_follower_count)
    if is_true:
      clear()
      print(logo)
      score += 1
      print(f"You are right. Current Score: {score}")
    else:
      should_cont = False
      print(f"Sorry! That is wrong. Your score is {score}")
game()
