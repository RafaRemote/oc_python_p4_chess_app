""" model for the menus"""

start_menu = ['create a new tournament',
              'choose en existing tournament'
              ]


all_tournaments_menu = ['Previous',
                        'Create new tournament',
                        'Quit'
                        ]

tournament_menu = ['Show All Tournaments',
                   'Add players',
                   'Enter score for last round played',
                   'Rounds details',
                   'Matches details',
                   'Players menu',
                   'Quit'
                   ]


class MenuModel:
    def __init__(self):
        self.start_menu = start_menu
        self.all_tournaments_menu = all_tournaments_menu
        self.tournament_menu = tournament_menu

    def __call__(self):
        return self
