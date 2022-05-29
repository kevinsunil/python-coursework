#Step 1 
import random
from hangman_words import word_list
from hangman_art import logo
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
print(logo)
word = random.choice(word_list)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
from hangman_art import stages
check=[]
for _ in range(len(word)):
    check += "_"
print(f"{' '.join(check)}")
gameover = 0
lives =6 
while(gameover == 0):
  character = input("Guess a character: ").lower()
  if len(character) > 1:
    print("wrong input enter only a single character")
  else:
    check3 = 0
    for char in range (0,len(word)):
      if word[char] == character:
        check[char]= character
        check3 += 1
      # else:
      #   if check[char] == '_':
      #     check[char]= "-"
      #   else:
      #     check[char] = check[char]
  if check3 == 0:
    lives -=1
    if lives == 0:
      print(stages[lives])
      print(f"you lost.... the word was {word}.. Game Over")
      gameover =1
    else:
      print("oops you lost a life")
      print(stages[lives])
      print(f"{' '.join(check)}")
  else:
    print(f"{' '.join(check)}")
    check2 =0
    for char in range(0,len(word)):
      if word[char] != check[char]:
        check2 += 1
    if check2 == 0:
      print("Yay you guessed the word")
      gameover += 1
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
