""" Input_player view """

import os
import time

from termcolor import colored


class InputPlayerView:
    """
    Class to represent a page to retreive user inputs for players
    ...

    Attributes
    ----------
    name: list
        list of strings, player names
    surname: list
        list of strings, player surnames
    year_birth: list
        list of int, player year of birth
    gender: list
        list of strings, player gender('m' or 'w')
    elo: list
        list of int: player elos

    Methods
    -------
    get_att(self, counter, att):
        return user inputs for attributes

    call(self):
        calls get_att(self, counter, att) until 8 series of inputs

    """

    def __init__(self):
        """
        Constructs attributes for InputPlayerView object.

        Parameters
        ----------
        none

        """

        self.name = []
        self.surname = []
        self.year_birth = []
        self.gender = []
        self.elo = []

    def get_att(self, counter, att):
        """
        prints questions, waiting for user inputs
        appending user inputs to the attributes lists

        Parameters
        ----------
        counter: int
            represent the number of player entered
        att: str
            represent attributes for which a user input is asked

        Returns
        -------
        no return

        """

        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored('      Enter infos about the players'.upper(), 'magenta'))
        print()
        print(f'Yet, you entered {counter} on 8')
        print()
        print(f'Still {8 - counter} player info to enter')
        print()
        i = 0
        while i < 1:
            if att == "name":
                name = input('Enter the name of the player: ')
                if len(name) == 0 or len(name) > 30:
                    print(colored('Name min length is one. Name max length is 30', 'red'))
                else:
                    counter += 1
                    self.name.append(name)
                    i += 1
            elif att == "surname":
                surname = input('Enter the surname of the player: ')
                if len(surname) == 0 or len(surname) > 30:
                    print(colored('Surname min length is one. Name max length is 30', 'red'))
                else:
                    counter += 1
                    self.surname.append(surname)
                    i += 1
            elif att == 'year_birth':
                i = 0
                while i < 1:
                    try:
                        year = input('Year of Birth ? ')
                        if 1900 <= int(year) <= 2010:
                            i += 1
                        else:
                            print(colored('Min year is 1900, max year is 2010', 'red'))
                    except ValueError:
                        print(colored('You need to type a four-digits composite number', 'red'))
                counter += 1
                self.year_birth.append(year)
            elif att == 'gender':
                choices = ['m', 'w']
                i = 0
                while i < 1:
                    gender = input('Enter the gender: m or w: ')
                    if gender not in choices:
                        print(colored('You need to choose either \'w or \'m', 'red'))
                    else:
                        i += 1
                        counter += 1
                        self.gender.append(gender)
            elif att == 'elo':
                i = 0
                while i < 1:
                    try:
                        elo = input('Elo ? ')
                        if 1000 <= int(elo) <= 3000:
                            i += 1
                        else:
                            print(colored('Min ELO is 1000, max year is 3000', 'red'))
                    except ValueError:
                        print(colored('You need to type a four-digits composite number', 'red'))
                counter += 1
                self.elo.append(elo)

    def __call__(self):
        """
        prints informations about:
            how many players have been entered
            message when 8 players have been entered

        Parameters
        ----------
        none

        Returns
        -------
        instance of InputPlayerView

        """

        counter = 0
        while counter < 8:
            att_lst = ['name', 'surname', 'year_birth', 'gender', 'elo']
            [self.get_att(counter, i) for i in att_lst]
            counter += 1
        if counter == 8:
            print()
            print(colored(f'You have entered the {counter} players', 'green'))
            time.sleep(.5)
            print()
            print(colored('Saving informations...', 'green'))
            print()
            time.sleep(.5)
            os.system('cls' if os.name == 'nt' else 'clear')
        return self
