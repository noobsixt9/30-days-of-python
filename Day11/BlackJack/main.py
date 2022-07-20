############### Blackjack Project #####################
import random
from art import logo
from replit import clear



def deal_card():
  """ returns one random card from list """
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
  
def calculate_score(card_list):
  """calculate the total sum"""
  if sum(card_list) > 21 and len(card_list) == 2:
    return 0
  if 11 in card_list and sum(card_list) > 21:
    card_list.remove(11)
    card_list.append(1)  
  return sum(card_list)

def compare(user_score, computer_score):
  """Compares user score and computer score"""
  if user_score > 21 and computer_score > 21:
    return "You lose. You went over  😤"
    
  if user_score == computer_score:
    return "It's a draw 🙃"
  elif computer_score == 0:
    return "You lose. Computer got a blackjack 😱"
  elif user_score == 0:
    return "You win. You got a blacjack 😎"
  elif user_score > 21:
    return "You lose. You went over 😭 "
  elif computer_score > 21:
    return "You win. Computer went over 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose  😤"
def play_game(): 
  
  print(logo)
  
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    score_check_user = calculate_score(user_cards)
    score_check_computer = calculate_score(computer_cards)
    print(f"\tYour cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"\tComputer's first card: {computer_cards[0]}")
    
    if score_check_computer == 0 or score_check_user == 0 or score_check_user > 21:
      is_game_over = True
    else:
      opt = input("Type 'y' to add another card and 'n' to pass: ")
      if opt == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True   
  
  while score_check_computer != 0 and score_check_computer < 17:
    computer_cards.append(deal_card())
    score_check_computer = calculate_score(computer_cards)
  print(f"\tYour final hand: {user_cards}, final score: {score_check_user}")
  print(f"\tComputer's final hand: {computer_cards}, final score: {score_check_computer}")
    
  print(f"{compare(score_check_user, score_check_computer)}")
while input("\nDo you want to play a game of BlackJack('y' for yes and 'n' for no): ") == "y":
    clear()
    play_game()
