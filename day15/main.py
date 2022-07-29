from recipe import MENU
from recipe import resources
profit = 0
machine_stop = False

def resource_check(order_ingredients):
  for i in resources:
    if (resources[i] < order_ingredients[i]):
      print(f"Sorry there is not enough {i}")
      return False
  return True

def process_cost():
  print("Please Enter the Coins:")
  total = int(input("Enter the amount of Pennies: "))*0.01
  total += int(input("Enter the amount of Nickels: "))*0.05
  total += int(input("Enter the amount of Dimes: "))*0.1
  total += int(input("Enter the amount of Quarters: "))*0.25
  return total

def transaction(user_amount,cost):
  global profit
  if user_amount >= cost :
    profit += cost
    change = round(user_amount - cost,2)
    if change != 0 :
      print(f"Here's your balance of ${change}")
      return True
  else:
    print("Not enough money, payment refunded")
    return False
def make_coffee(drink_name, order_ingredients):
  for item in order_ingredients:
    resources[item] -= order_ingredients[item]
  print(f"Your order of {drink_name} has been prepared")

while (machine_stop != True):
  user_input = input("What would you like (espresso/latte/cappuccino): ").lower()
  if (user_input ==  'off'):
    machine_stop = True
  elif (user_input == 'report'):
    for i in resources:
      print(f"{i} : {resources[i]}")
    print(f"money : {profit}")
  else:
    drink = MENU[user_input]
    if resource_check(drink["ingredients"]):
      print(f'Please pay{drink["cost"]}')
      payment_recieved = process_cost()
      if transaction(payment_recieved,drink["cost"]):
        make_coffee(user_input,drink["ingredients"])
