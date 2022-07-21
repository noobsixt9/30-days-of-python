############### Blackjack Project #####################
import random
from replit import clear
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(card_list):
  if sum(card_list) == 21 and len(card_list) == 2:
    return 0
  if 11 in card_list and sum(card_list) > 21:
    card_list.remove(11)
    card_list.append(1)
  return sum(card_list)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose."
    
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Computer got a blackjack. You lose."
  elif user_score == 0:
    return "You got a blackjack. You win."
  elif computer_score > 21:
    return "Computer went over. You win."
  elif user_score > 21:
    return "You went over. You lose"
  elif user_score > computer_score:
    return "You win."
  else:
    return "You lose."
def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_end = False
  
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_end:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"\tYour cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"\tComputer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_end = True
    else:
      
      opt = input("Do you want to add another card or pass (type 'y' for yes and 'n' for no): ")
      if opt == "y":
        user_cards.append(deal_card())
      else:
        is_game_end = True
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  print(f"\tYour final cards: {user_cards}, final score: {user_score}")
  print(f"\tComputer's final cards: {computer_cards}, final score: {computer_score}")
  
  print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack?(Type 'y' for yes and 'n' for no): ") == "y":
  clear()
  play_game()
