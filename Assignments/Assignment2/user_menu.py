from store import Store
import pathlib


class UserMenu:
    def __init__(self):
        self.store = Store()
        self.menu_items = {"1": self.process_web_orders, "2": self.check_inventory}

    def print_options(self):
        print("Main Menu")
        print("1. Process Web Orders")
        print("2. Check Inventory")
        print("3. Exit")

    def main_menu(self):
        while True:
            self.print_options()
            choice = ""
            while True:
                choice = input()
                if choice == "0" or choice in self.menu_items:
                    break
                print(f"{choice} is not a valid choice")
            if choice == "0":
                break
            self.menu_items[choice]()

        print("Closing program...")




    def process_web_orders(self):
        print("Please input the path of your order file")
        while True:
            choice = pathlib.Path(input())
            if not choice.is_dir() and choice.exists():
                break
            print(f"{choice} is not a valid choice")
        self.store.process_orders(choice)

    def check_inventory(self):
        for item in self.store.check_inventory():
            print(f"{item[3].value()} | {item[0]} | {item[1]} | {item[2]}")


menu = UserMenu()
menu.main_menu()


