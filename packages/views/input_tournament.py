""" Input_tournament view """

import time
import os

from termcolor import colored


class InputTournamentView:
    """
    Class to represent a page to retrieve user inputs for a tournament
    ...

    Attributes
    ----------
    place: str
        default set: ''
        place where the tournament takes place
    title: str
        default set: ''
        title of the tournament
    time_control: str
        default set: ''
        type of time control for the tournement
    description: str
        default set: ''
        description of the tournament

    Methods
    -------
    display_title(self):
        prints title
    get_inputs(self):
        assign user inputs to self attributes
    call(self):
        returns instance of InputTournamentView

    """

    def __init__(self):
        """
        Constructs attributes for InputTournamentView object.

        Parameters
        ----------
        none

        """

        self.place = ''
        self.title = ''
        self.time_control = ''
        self.description = ''

    def display_title(self):
        """ prints string, no return """

        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored('      ENTER TOURNAMENT INFORMATIONS',
                      'magenta'
                      ))
        print()
        print()

    def check_len(self, string, max):
        """
        checks length of a str

        Parameters
        ----------
        name: string
            string
        max: int
            represents max length for a string

        Returns
        -------
        boolean

        """

        if(len(string) == 0):
            print(colored('You entered nothing, you need to enter something.', 'red'))
            time.sleep(1)
            return True
        if len(string) > max:
            print(colored(f'You have entered too many characters, the max is {max}', 'red'))
            time.sleep(1)
            return True
        else:
            return False

    def get_inputs(self):
        """ assign values to self attributes from user inputs """

        self.display_title()
        i = 0
        while i < 1:
            place = input('Place the tournament is taking place [max: 20 characters]: ')
            if self.check_len(place, 20):
                i = 0
            else:
                self.place = place
                i += 1
        self.display_title()
        i = 0
        while i < 1:
            title = input('Title of the tournament [max: 20 characters]: ')
            if self.check_len(title, 20):
                i = 0
            else:
                self.title = title
                i += 1
        self.display_title()
        times = ['bullet', 'blitz', 'rapid']
        i = 0
        while i < 1:
            time_control = input('Enter time option: bullet, blitz or rapid: ')
            if time_control not in times:
                print(colored('the only options availabe are bullet, blitz or rapid.', 'red'))
                print('try again')
                i = 0
            else:
                self.time_control = time_control
                i += 1
        self.display_title()
        i = 0
        while i < 1:
            description = input('Enter a description for the tournament [max 500 characters]: ')
            if self.check_len(description, 500):
                i = 0
            else:
                self.description = description
                i += 1

    def __call__(self):
        """ calls self.get_inputs(), prints input, returns instance of InputTournamentView """

        self.get_inputs()
        self.display_title()
        print(colored('Saving tournament informations', 'green'))
        print()
        time.sleep(.5)
        input(colored('press return to go to the main menu', "blue"))
        return self
