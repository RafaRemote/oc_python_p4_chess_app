""" model for the menus"""



menus = {
        "HomeMenu" : [
            'create new tournament',
            'add players',
            'enter results',
            'show tournament ranking',
            'show tournament details'
        ]
}

list_of_menus =  [
            'HomeMenu',
]


class MenuModel:
    def __init__(self, name, choice):
        self.name = name,
        self.choice = choice
        self.options = []
       
    def __call__(self):
        print('MENUMODEL received:', self.__dict__)
        name_of_menu_received = self.__dict__.get('name')[0]
        choice = self.__dict__.get('choice')
        if choice is not None and not choice.isalpha():
            self.choice = int(choice)
        elif choice is not None and not choice.isnumeric():
            return ['error', self.name, 'your choice is not in the list of choice']
        if self.choice is not None and self.choice not in range(1, len(menus[name_of_menu_received]) + 1):
            return ['error', self.name, 'your choice is not in the list of choice']
   
        if name_of_menu_received  in list_of_menus:
            self.name = name_of_menu_received
            self.options = [option for option in menus[self.name]]
            print('menumodel returns ', self.__dict__)
            return self
        else:
            return ['error', self.name[0], 'did not find the menu asked for']

