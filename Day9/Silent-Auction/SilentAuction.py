from replit import clear
from art import logo

print(logo)

more_bidders = True
bidders = {}

def highest_bidder(bidding_record):
    highest_bid = 0
    bidder_name = ""
    for bidder in bidding_record:
      bids = bidding_record[bidder]
      if bids > highest_bid:
        highest_bid = bids
        bidder_name += bidder
    print(f"This auction's winner is {bidder_name} with {highest_bid} bid.")

while more_bidders:
  print("Welcome to silent auction program.")
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: "))
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  bidders[name] = bid
  if other_bidders == 'yes':
    clear()
  elif other_bidders == 'no':
    more_bidders = False
    highest_bidder(bidding_record=bidders)
