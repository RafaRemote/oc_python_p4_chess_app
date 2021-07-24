""" retrieve user inputs about tournament details """

import time
import os

from termcolor import colored


class InputTournamentView:
    """
    Class to represent a page of inputs for a tournament

    ...

    Attributes
    ----------
    place: function
        calls self.get_place()
    title: function
        calls self.get_title()
    time_control: function
        calls self.get_time_control()
    description: function
        calls self.get_description()

    Methods
    -------
    display_title(self):
        print title
    check_len(self, name, max):
        helper function
        check length of a string
    get_place(self):
        assign str value for attribute place
    get_title(self):
        assign str value for attribute title
    get_time_control(self):
        assign str value for attribute time_control
        from whithin a list
    get_description(self):
        assign str value for attribte description
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

        self.place = self.get_place()
        self.title = self.get_title()
        self.time_control = self.get_time_control()
        self.description = self.get_description()

    def display_title(self):
        """
        print string

        Parameters
        ----------
        none

        Returns
        -------
        none
        """

        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored('      ENTER TOURNAMENT INFORMATIONS',
                      'magenta'
                      ))
        print()
        print()

    def check_len(self, name, max):
        """
        check length of a str

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

        if(len(name) == 0):
            print(colored('You entered nothing, you need to enter something.', 'red'))
            time.sleep(1)
            return False
        if len(name) > max:
            print(colored(f'You have entered too many characters, the max is {max}', 'red'))
            time.sleep(1)
            return False
        else:
            return True

    def get_place(self):
        """
        print input

        Parameters
        ----------
        none

        Returns
        -------
        str
        """

        self.display_title()
        print()
        place = input('Place the tournament is taking place [max: 20 characters]: ')
        if self.check_len(place, 20):
            print()
            return place
        else:
            self.get_place()

    def get_title(self):
        """
        print input

        Parameters
        ----------
        none

        Returns
        -------
        str
        """

        name = input('Name of the tournament [max: 20 characters]: ')
        if self.check_len(name, 20):
            print()
            return name
        else:
            self.get_name()

    def get_time_control(self):
        """
        print string

        Parameters
        ----------
        none

        Returns
        -------
        none
        """

        times = ['bullet', 'blitz', 'rapid']
        time_control = input('Enter time option: bullet, blitz or rapid: ')
        print()
        while time_control.lower() not in times:
            print(colored('the only options availabe are bullet, blitz or rapid.', 'red'))
            print('try again')
            print()
            return self.get_time_control()
        else:
            return time_control

    def get_description(self):
        """
        print string

        Parameters
        ----------
        none

        Returns
        -------
        str
        """

        description = input('Enter a description for the tournament [max 500 characters]: ')
        if self.check_len(description, 500):
            return description
        else:
            self.get_description()

    def __call__(self):
        """
        print string

        Parameters
        ----------
        none

        Returns
        -------
        instance of InputTournamentView
        """

        print()
        input(colored('press return to go to the main menu', "blue"))
        return self
