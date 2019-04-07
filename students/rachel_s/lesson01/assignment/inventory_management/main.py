"""Launches the user interface for the inventory management system
"""


import sys
import market_prices
import inventory
import furniture
import electric_appliances


def main_menu(user_prompt=None):
    """Main menu function
    """
    valid_prompts = {"1": add_new_item,
                     "2": item_info,
                     "q": exit_program}
    options = list(valid_prompts.keys())

    while user_prompt not in valid_prompts:
        options_str = ("{}" + (", {}") * (len(options)-1)).format(*options)
        print("Please choose from the following options ({options_str}):")
        print("1. Add a new item to the inventory")
        print("2. Get item information")
        print("q. Quit")
        user_prompt = input(">")
    return valid_prompts.get(user_prompt)


def get_price(item_code):
    """Accepts item code and returns item price
    """
    print("Get price for {item_code}")


def add_new_item():
    """Adds a new item to the inventory based on user-inputted
    item code, description, and rental price.
    """
    # global __full_inventory__
    item_code = input("Enter item code: ")
    item_description = input("Enter item description: ")
    item_rental_price = input("Enter item rental price: ")

    # Get price from the market prices module
    item_price = market_prices.get_latest_price(item_code)

    is_furniture = input("Is this item a piece of furniture? (Y/N): ")
    if is_furniture.lower() == "y":
        item_material = input("Enter item material: ")
        item_size = input("Enter item size (S,M,L,XL): ")
        new_item = furniture.Furniture(item_code, item_description,
                                       item_price,
                                       item_rental_price,
                                       item_material, item_size)

    else:
        is_electric_appliance = input("Is this item an electric "
                                      "appliance? (Y/N): ")
        if is_electric_appliance.lower() == "y":
            item_brand = input("Enter item brand: ")
            item_voltage = input("Enter item voltage: ")
            new_item = electric_appliances.ElectricAppliances(
                item_code, item_description, item_price,
                item_rental_price, item_brand, item_voltage)
        else:
            new_item = inventory.Inventory(
                item_code, item_description, item_price,
                item_rental_price)
    __full_inventory__[item_code] = new_item.return_as_dictionary()
    print("New inventory item added")


def item_info():
    """Takes an item code and returns the inventory values for that
    item
    """
    item_code = input("Enter item code: ")
    if item_code in __full_inventory__:
        print_dict = __full_inventory__[item_code]
        for key, value in print_dict.items():
            print("{}:{}".format(key, value))
    else:
        print("Item not found in inventory")


def exit_program():
    """Exits the menu"""
    sys.exit()


if __name__ == '__main__':
    __full_inventory__ = {}
    while True:
        print(__full_inventory__)
        main_menu()()
        input("Press Enter to continue...........")
