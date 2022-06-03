from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to the Secret Auction!!!!")
auction_bid = {}
check_continue = True
while check_continue == True:
  bidder = input("Enter the bidders name: ")
  bid = int(input("Enter the bidding amount: $"))
  auction_bid[bidder] = bid
  decision = input("Is there any more bids? enter yes or no: ").lower()
  if decision == 'yes':
    clear()
  else:
    check_continue = False
max_bid = 0
max_bidder = ''
for key in auction_bid:
  if auction_bid[key] > max_bid:
    max_bid = auction_bid[key]
    max_bidder = key
clear()
print(f"The winner is {max_bidder} with a bid of ${max_bid}")
