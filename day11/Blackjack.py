############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
import random
from art import logo
from replit import clear


def deal_cards():
    cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)
def calc_score(cards):
    score = sum(cards)
    if (score == 21 and len(cards) == 2):
       return 0;
    elif 11 in cards and score >21:
       cards.remove(11)
       cards.append(1)
       return sum(cards)
    else:
      return score
def check_status(score1, score2):
    if score1 == 0 and score2 !=0:
      print("It's a Blackjack you won....")
    elif score2 == 0 and score1 !=0 :
      print("Dealer has a Blackjack you lost....")
    elif score2 == score1:
      print("It's a push. Game drawn")
    elif score2 > score1 and score2<=21 and score1<21 :
      print("Dealer has won")
    elif score1 > score2 and score1<=21 and score2<21 :
      print("You have won")
    elif score2 > 21 and score1<=21 :
      print("Dealer has bust, you won")
    elif score1 > 21:
      print("You have bust , Dealer has won")    
  
    
def game():
    print(logo)
    game_over = False
    user_cards = []
    computer_cards = []
    for i in range (2):
      user_cards.append(deal_cards()) 
      computer_cards.append(deal_cards())
    while (game_over == False):
      user_score  = calc_score(user_cards)
      computer_score  = calc_score(computer_cards)
      print(f"Your cards: {user_cards} and your score: {user_score}")
      print(f"Dealer first card: {computer_cards[0]}")
      if(user_score!= 0 and user_score < 21):
        user_choice = input("Do you want to draw another card? ").lower()
        if (user_choice == 'yes' or user_choice == 'y'):
          user_cards.append(deal_cards())
          user_score = calc_score(user_cards)
        else:
          game_over = True
      else:
          game_over = True
    while(computer_score != 0 and computer_score<16):
      computer_cards.append(deal_cards())
      computer_score = calc_score(computer_cards)
    print(f"Your final set: {user_cards} and score: {user_score} ")
    print(f"Dealer's final set: {computer_cards} and score: {computer_score} ")
    check_status(user_score, computer_score)

user_input = input("Do you want to play a game of blackjack? ").lower()
if(user_input == 'yes' or user_input == 'y'):
  clear()
  game()
