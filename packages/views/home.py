""" docstrings """

from packages.controllers.welcome import WelcomeController
from packages.controllers.tournament import TournamentController

class HomeMenu:
    def __init__(self):
        self.name = 'HomeMenu'

    def welcome(self):
        welcome = WelcomeController()
        welcome()

    def __call__(self):        
        tournament = TournamentController()
        tournament()    
