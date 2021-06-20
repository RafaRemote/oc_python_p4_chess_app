""" model for the menus"""

menus = {
        "homemenu": [
            'create tournament',
            'add players',
            'enter results for round1',
            'enter results for round2',
            'enter results for round3',
            'enter results for round4',
            'show ranking per score',
            'show players per alphabetical order',
            'show opponents'
        ]
}


class MenuModel:
    def __init__(self, name, choice):
        self.name = name
        self.choice_number = choice
        self.choice_list = menus[self.name.lower()]

    def __call__(self):
        return self
