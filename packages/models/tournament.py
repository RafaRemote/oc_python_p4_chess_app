import datetime
from packages.models.player import PlayerModel

TOTALROUNDS = 4
PLACE = 'Paris'

players = [
    PlayerModel(['Simpsons', 'Homer', 1980, 'm', 1000]),
    PlayerModel(['Simpsons', 'Marge', 1985, 'm', 2000]),
    PlayerModel(['Simpsons', 'Bart', 2010, 'm', 500]),
    PlayerModel(['Simpsons', 'Lisa', 2011, 'm', 3000]),
    PlayerModel(['Simpsons', 'Maggie', 2018, 'm', 1500]),
    PlayerModel(['Nahasapee', 'Apu', 1970, 'm', 3000]),
    PlayerModel(['Montgomery', 'Charles', 1900, 'm', 5000]),
    PlayerModel(['Flanders', 'Ned', 1880, 'm', 2000])
]
choice_of_times = ['bullet', 'blitz', 'rapid']


date = datetime.datetime.now().strftime("%a %d %B %Y")

tournament_list = []
class TournamentModel:
    def __init__(self, obj_from_controller, obj_player):
        if obj_from_controller is not None:
            self.name = obj_from_controller.__dict__['name']
            self.place = PLACE
            self.date = date
            self.total_rounds = TOTALROUNDS
            self.rounds = []
            self.players = []
            self.time_control = obj_from_controller.__dict__['time']
            self.description = obj_from_controller.__dict__['description']
        else:
            self.name = None
            self.place = None
            self.date = None
            self.total_rounds = None
            self.rounds = []
            self.players = None
            self.time_control = None
            self.description = None

        if obj_player is not None:
            self.players = obj_player

    def add_a_round(self, instance_of_round):
        tournament_list[0].__dict__.get('rounds').append(instance_of_round)
        return(tournament_list[0])

    def __call__(self):
        players.append(self.players)
        if self.time_control is not None and self.time_control not in choice_of_times:
            return ['error', self.__class__.__name__, f'{self.time_control} does not match with the propositions']
        else: 
            self.time_control = self.time_control
        tournament_list.append(self)
        return self

    def add_round(self, round):
        self.rounds.append(round)

