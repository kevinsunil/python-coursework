from art import logo
from art import vs
import random
from game_data import data
print(logo)
score = 0
i=0
while(i==0):
  print(f"Score: {score}")
  print("Who has more followers on Instagram? ")
  number = random.randint(0,len(data)-1)
  print(f"{data[number]['name']} a {data[number]['description']} ")
  print(vs)
  number1 = random.randint(0,len(data)-1)
  print(f"{data[number1]['name']} a {data[number1]['description']} ")
  choice =  int(input(f"Enter 1 for {data[number]['name']} and 2 for {data[number1]['name']} "))
  if (choice == 1 and data[number]['follower_count']>=data[number1]['follower_count']):
    score += 1
  elif (choice == 1 and data[number]['follower_count']< data[number1]['follower_count']):
    print("You lost")
    i=1
  elif (choice == 2 and data[number]['follower_count']>= data[number1]['follower_count']):
    print("You lost")
    i =1
  else:
    score += 1
print(f"Your final score: {score}")
