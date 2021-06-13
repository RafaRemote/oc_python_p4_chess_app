import datetime



players = [

]

choice_of_times = ['bullet', 'blitz', 'rapid']

TOTALROUNDS = 4
PLACE = 'Paris'

date = datetime.datetime.now().strftime("%a %d %B %Y")
class TournamentModel:
    def __init__(self, obj_from_controller):
        print(obj_from_controller.__dict__)
        self.name = obj_from_controller.__dict__['name']
        self.place = PLACE
        self.date = date
        self.total_rounds = TOTALROUNDS
        self.rounds = []
        self.players = []
        self.time_control = obj_from_controller.__dict__['time']
        self.description = obj_from_controller.__dict__['description']

    def __call__(self):
        if self.time_control not in choice_of_times:
            return ['error', self.__class__.__name__, f'{self.time_control} does not match with the propositions']
        else: 
            for i,j in self.__dict__.items():
                print(i, ':', j)
    
    def add_player(self, player):
        self.players.append(player)

    def add_round(self, round):
        self.rounds.append(round)

