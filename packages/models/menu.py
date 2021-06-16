""" model for the menus"""


menus = {
        "homemenu" : [
            'create new tournament',
            'add players',
            'enter results',
            'show tournament ranking',
            'show tournament details'
        ]
}


class MenuModel:
    def __init__(self, name, choice):
        self.name = name
        self.choice = choice
        self.choice_list = menus[self.name]
       
    def __call__(self):
        return self






      
        # if choice is not None and not choice.isalpha() and choice != '':
        #     self.choice = int(choice)
        # elif choice is not None and not choice.isnumeric():
        #     return ['error', self.name, 'your choice is not in the list of choice']
        # else:
        #     self.choice = None
        # if self.choice is not None and self.choice not in range(1, len(menus[name_of_menu_received]) + 1):
        #     return ['error', self.name, 'your choice is not in the list of choice']
   
        # if name_of_menu_received  in list_of_menus:
        #     self.name = name_of_menu_received
        #     self.options = [option for option in menus[self.name]]
        #     return self
        # else:
        #     return ['error', self.name[0], 'did not find the menu asked for']

# return ['error', self.name[0], 'did not find the menu asked for']