import random
from art import logo
print(logo)
game_level = input("Do you want to play in 'easy' or 'hard' level? ").lower()
if (game_level == 'easy'):
  i =10
elif (game_level == 'hard'):
  i =5

def game():
  global i
  number = random.randint(1,100)
  while(i>0):
    guess = int(input("Enter Your Guess: "))
    if(guess == number):
      print("Yay you guessed it")
      break
    elif(guess>number):
      print("Too High")
      i -= 1
    else:
      print("Too Low")
      i -= 1
    print(f"You have {i} guesses left")
  print(f"Sorry you lost the number was: {number}")
print("I am guessing a number which lies from 1 to 100")
game()
