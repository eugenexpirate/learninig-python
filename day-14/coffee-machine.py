import os

machine_resources = {
    'water': 200,
    'milk': 500,
    'coffee': 750,
    'money': 2.0
}

coffee_menu = \
{   
    'latte': {
        'water': 100,
        'milk': 50,
        'coffee': 75,
        'price': 1.0
    },
    'espresso': {
        'water': 25,
        'milk': 0,
        'coffee': 75,
        'price': 0.5
    },
    'cappuchino': {
        'water': 80,
        'milk': 70,
        'coffee': 75,
        'price': 1.1
    }
}

coins = {
    'quarter': 0.25,
    'dime': 0.1,
    'nickle': 0.05,
    'pennie': 0.01,
    'end': 0.0
}


def is_resource_available(coffee_type):
    coffee = coffee_menu[coffee_type]
    
    if machine_resources['coffee'] < coffee['coffee']:
        print("Sorry there is no enough coffee")
        return False
    if machine_resources['milk'] < coffee['milk']:
        print("Sorry there is no enough milk")
        return False
    if machine_resources['water'] < coffee['water']:
        print("Sorry there is no enough water")
        return False

    return True

def print_report():
    print(f"Water: {machine_resources['water']}ml")
    print(f"Milk: {machine_resources['milk']}ml")
    print(f"Coffee: {machine_resources['coffee']}g")
    print(f"Money: ${machine_resources['money']}")
    input("Press Enter to continue...")


while True:
    os.system('clear')
    print("What would you like? (espresso/latte/cappuchino):")
    answer = ""
    while answer not in ['espresso', 'latte', 'cappuchino', 'off', 'report']:
        answer = input() # .lower()
    
    if answer == 'off':
        break

    if answer == 'report':
        print_report()
        continue

    if not is_resource_available(answer):
        input("Press Enter to continue...")
        continue

    print("Insert conis: Type ", end="")
    for coin in coins.keys():
        print(f"'{coin}'", end=", ")
    print(" ('end' to end)")
    inserted_coin = ""

    money = 0.0
    change = 0.0
    while True:
        while inserted_coin not in coins.keys():
            inserted_coin = input()
        if inserted_coin == 'end':
            break
        money += coins[inserted_coin]
        inserted_coin = ""
    
    print("Total inserted $", money)

    if coffee_menu[answer]['price'] > money:
        print("Sorry that's not enough money. Money refunded.")
        input("Press Enter to continue...")
        continue
    else:
        change = money - coffee_menu[answer]['price']
        change = round(change, 2)
        machine_resources['money'] += money - change
        machine_resources['coffee'] -= coffee_menu[answer]['coffee']
        machine_resources['milk'] -= coffee_menu[answer]['milk']
        machine_resources['water'] -= coffee_menu[answer]['water']

    print(f"Here is your {answer}")
    if change > 0.0:
        print(f"Refund ${change}:")
        while change > 0:
            change = round(change, 2)
            if change >= coins['quarter']:
                print("quarter")
                change -= coins['quarter']
                continue
            elif change >= coins['dime']:
                print("dime")
                change -= coins['dime']
                continue
            elif change >= coins['nickle']:
                print("nickle")
                change -= coins['nickle']
                continue
            else:
                print("pennie")
                change -= coins['pennie']
                continue
    input()




    


