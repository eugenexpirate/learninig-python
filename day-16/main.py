from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

import os

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()



while True:
    os.system('clear')
    print(f"What would you like?: ({menu.get_items()})")
    answer = ""
    while answer not in ['espresso', 'latte', 'cappuchino', 'off', 'report']:
        answer = input() # .lower()
    
    if answer == 'off':
        break

    if answer == 'report':
        coffee_maker.report()
        money_machine.report()
        input("Press Enter to continue...")
        continue

    menu_item = menu.find_drink(answer)
    if menu_item == None:
        input()
        continue
    
    if not coffee_maker.is_resource_sufficient(menu_item):
        input()
        continue
    
    if not money_machine.make_payment(menu_item.cost):
        input()
        continue

    coffee_maker.make_coffee(menu_item)
    input()