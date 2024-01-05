from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    user_choice = str(input(f' What would you like? ({menu.get_items()}): ')).strip().lower()
    if user_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif user_choice == 'off':
        break
    elif user_choice:
        drink = menu.find_drink(user_choice)
        if drink is not None and coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
