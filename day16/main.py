from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

rep = CoffeeMaker()
mon = MoneyMachine()
men = Menu()
machine_stop = False
while not machine_stop:

    user_input = input(f"What would you like {men.get_items()}: ").lower()
    if user_input == 'off':
        machine_stop = True
    elif user_input == 'report':
        rep.report()
        mon.report()
    else:
        drink = men.find_drink(user_input)
        if rep.is_resource_sufficient(drink):
            print(f"Please pay: ${drink.cost} ")
            if mon.make_payment(drink.cost):
                rep.make_coffee(drink)
