""" menu model """

start_menu = ['Create a New Tournament',
              'Choose an Existing Tournament'
              ]

all_tournaments_menu = ['Main Menu',
                        'Create new tournament',
                        'Quit'
                        ]

tournament_menu = ['Main Menu',
                   'Add Players',
                   'Start Tournament',
                   'Start Next Round',
                   'Enter Scores for Current Round',
                   'Rounds Details',
                   'Matches Details',
                   'Players Menu',
                   'Show Opponents',
                   'Quit'
                   ]


class MenuModel:
    """
    Class for represent a menu

    ...

    Attributes
    ----------
    none

    Methods
    -------
    call:
        returns self
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the menus.

        Parameters
        ----------
        start_menu: list
            list of str represents the menu for the main menu at start
        all_tournaments_menu: list
            list of str represents the menu for the list of tournaments
        tournament_menu: list
            list of str represents the menu for one tournament

        """

        self.start_menu = start_menu
        self.all_tournaments_menu = all_tournaments_menu
        self.tournament_menu = tournament_menu

    def __call__(self):
        return self
