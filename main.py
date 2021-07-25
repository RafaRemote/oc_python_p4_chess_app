""" Application entry point """

from packages.controllers.menu import MenuController


if __name__ == "__main__":
    welcome = MenuController.welcome()
    welcome()
