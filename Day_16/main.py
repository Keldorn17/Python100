from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main() -> None:
    menu: Menu = Menu()
    coffee_maker: CoffeeMaker = CoffeeMaker()
    money_machine: MoneyMachine = MoneyMachine()

    while True:
        response: str = input(f"What would you like? ({menu.get_items()}): ").lower()
        if response == "off":
            break
        elif response == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            menu_item = menu.find_drink(response)
            if coffee_maker.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)


if __name__ == '__main__':
    main()
