import machine_details


def print_report(machine_recourses: dict) -> None:
    print(f"Water: {machine_recourses['water']}ml")
    print(f"Milk: {machine_recourses['milk']}ml")
    print(f"Coffee: {machine_recourses['coffee']}g")
    print(f"Money: ${machine_recourses['money']}")


def check_change(ordered_item_name: str, menu: dict) -> bool:
    print("Please insert coins.")
    sum_money: int = sum([int(input("How many quarters?: ")) * .25, int(input("How many dimes?: ")) * .1,
                          int(input("How many nickles?: ")) * .05, int(input("How many pennies?: ")) * .01])
    cost: int = menu[ordered_item_name]["cost"]
    if sum_money > cost:
        print(f"Here is ${'{:.2f}'.format(sum_money - cost)} in change.")
    elif sum_money < cost:
        print("Sorry that's not enough money. Money refunded.")
    return sum_money >= cost


def check_resources_sufficient(machine_recourses: dict, ordered_item_name: str, menu: dict) -> bool:
    for ingredient in menu[ordered_item_name]["ingredients"]:
        if menu[ordered_item_name]["ingredients"][ingredient] > machine_recourses[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


def make_coffee(machine_recourses: dict, ordered_item_name: str, menu: dict) -> None:
    for ingredient in menu[ordered_item_name]["ingredients"]:
        machine_recourses[ingredient] -= menu[ordered_item_name]["ingredients"][ingredient]
    machine_recourses["money"] += menu[ordered_item_name]["cost"]
    print(f"Here is your {ordered_item_name} ☕. Enjoy!")


def main() -> None:
    items: list = ["espresso", "latte", "cappuccino"]
    recourses: dict = machine_details.resources
    while True:
        ordered_item: str = input(f"What would you like? ({items[0]}/{items[1]}/{items[2]}): ").lower()
        if ordered_item == "report":
            print_report(recourses)
        elif ordered_item == "off":
            break
        elif ordered_item in items:
            if check_resources_sufficient(recourses, ordered_item, machine_details.MENU) and check_change(ordered_item, machine_details.MENU):
                make_coffee(recourses, ordered_item, machine_details.MENU)
        else:
            print("Invalid input. Try again.")


if __name__ == '__main__':
    main()
