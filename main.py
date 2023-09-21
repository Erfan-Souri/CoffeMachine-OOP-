from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

device_on = True
while device_on:
    options = menu.get_items()
    order_name = str(input(f"what would you like? {options}: "))
    menu_object = menu.find_drink(order_name)

    if order_name == "report":
        coffe_maker.report()
        money_machine.report()

    elif order_name == "off":
        print("coffe machine is shutting down for maintenance!\nGoodbye!")
        device_on = False

    else:
        if coffe_maker.is_resource_sufficient(menu_object) and money_machine.make_payment(menu_object.cost):
            coffe_maker.make_coffee(menu_object)
