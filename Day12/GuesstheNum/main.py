#----Number Guessing Game------
import random
from art import logo

hard = 5
easy = 10

def difficulty():
  """set difficulty level"""
  level = input("Choose difficulty level. Type 'easy'or'hard': ")
  if level == "hard":
    return hard
  else:
    return easy
def check(guess,answer,turns):
  """check answer and track count of attempts"""
  if guess > answer:
    print("Too high")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns -  1
  else:
    print(f"You got it. Answer was {answer}")

def play_game():
  print(logo)
  print("Welcome to Number Guessing Game!")
  print("I am thinking of a number between 1 and 100.")

  answer = random.randint(1,100)
  turns = difficulty()
  print(f"Psst! answer is {answer}")
  guess = 0
  while guess != answer:
    print(f"You have {turns} left")
    guess = int(input("Make a guess: "))

    turns = check(guess, answer, turns)
    if turns == 0:
      print("You have run out of attempts. You lose")
      return
    elif guess != answer:
      print("Guess again: ")

play_game()
