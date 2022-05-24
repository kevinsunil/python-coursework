import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
userchoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
comp = random.randint(0,2)
i=0
if userchoice == 0:
  print(f"\n user chose {rock}")
elif userchoice == 1:
  print(f"\n user chose {paper}")
elif userchoice == 2:
  print(f"\n user chose {scissors}")
else:
  print("\n Wrong choice entered")
  i += 1
while(i == 0):
  if comp == 0:
    print(f"\n computer chose {rock}")
  elif comp == 1:
    print(f"\n computer chose {paper}")
  else:
    print(f"\n computer chose {scissors}")

  if ((userchoice == 0 and comp == 2) or (userchoice == 1 and comp == 0) or (userchoice == 2 and comp == 1) ):
    print("You won... Yay!!!!")
  elif(userchoice == comp):
    print("It's a draw..... No one won")
  else:
    print("You lost....oops you can try again")
  i += 1
