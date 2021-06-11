""" controller returning a view for the menus """

from packages.models.menu import MenuModel

class MenuController:
    def __init__(self, *args):
        for j in args:
            self.__dict__['name'] = j

    def __call__(self):
        menuModel = MenuModel(self.name)
        menuModel()

