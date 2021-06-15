import datetime
from os import name
from time import strftime

from packages.models.player import PlayerModel
from packages.models.match import MatchModel 


players = [
    PlayerModel('Simpsons', 'Homer', 1980, 'm', [], 1000, 0),
    PlayerModel('Simpsons', 'Marge', 1985, 'w', [], 2000, 0),
    PlayerModel('Simpsons', 'Bart', 2010, 'm', [], 500, 0),
    PlayerModel('Simpsons', 'Lisa', 2011, 'w', [], 3000, 0),
    PlayerModel('Simpsons', 'Maggie', 2018, 'w', [], 1500, 0),
    PlayerModel('Nahasapee', 'Apu', 1970, 'm', [], 3000, 0),
    PlayerModel('Montgomery', 'Charles', 1900, [], 'm', 5000, 0),
    PlayerModel('Flanders', 'Ned', 1880, 'm', [], 2000, 0)
]


class RoundModel:
    def __init__(self, tournament_name):
        self.tournmanent_name = tournament_name
        self.name = None
        self.start_date = None
        self.end_date = None
        self.matches = dict()
        self.players = sorted(players, key=lambda x: x.elo, reverse=True)


    def round(self):
        self.name = name
        self.start_date = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        
        for i in list_of_players:
            cleaned_list.append(i.__dict__.get('elo'))
            cleaned_list.append(i)
        newlist = sorted(list_of_players, key=lambda x: x.elo, reverse=True)
        high_group = newlist[:4]
        low_group = newlist[4:]
        
        for i in range(0, 4):
            self.matches.append( MatchModel(high_group[i], low_group[i], score1=0, score2=0))
        
        return self

    def round2(self, update):
        self.name = 'Round2'
        self.start_date = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        obj_round1 = update[0][0].__dict__.get('rounds')[0].__dict__.get('matches')
        obj_ranking = update[1]
        
        for i in obj_ranking:
                players_opponents[i[0]] = []
        
        for i in range(0, len(obj_round1)):
            player = obj_round1[i].__dict__.get('player1')[0]
            opponent = obj_round1[i].__dict__.get('player2')[0]
            players_opponents[player].append(opponent)    
            players_opponents[opponent].append(player)

        self.players = []

        for i in obj_ranking:
            self.players.append(i[0])

        for i in self.players:
            print(i.__dict__.get('surname'))

        players_ones = []
        players_twos = []

        for i in range(0, len(self.players)):
            
            if i%2 == 0:
                players_ones.append(self.players[i])
            elif i%2 != 0:
                players_twos.append(self.players[i])

        print('player ones')
        for i in players_ones:
            print('p1', i.__dict__.get('surname'))
        print()
        print('player twos')
        for i in players_twos:
            print('p2', i.__dict__.get('surname'))
        players_current_round = []


        for i in range(0, 4):
            if players_ones[i] not in players_current_round:
                if players_twos[i] not in players_opponents[players_ones[i]] and players_twos[i] not in players_current_round:
                    print('match ', players_ones[i].__dict__.get('surname') , ' // ', players_twos[i].__dict__.get('surname'))
                    players_current_round.append(players_ones[i])
                    players_current_round.append(players_twos[i])
                    for i in players_current_round:
                        print(i.__dict__.get('surname'))
                else:
                    players_twos[i+1]

     
       
        # for i in range(0, len(self.players)):            
        #     if i%2 == 0:
        #         player_one = self.players[i]
        #         if player_one not in players_current_round: 
        #             player_two = self.players[i+1]
        #             print('match before', player_one.__dict__.get('surname'), '//', player_two.__dict__.get('surname'))
        #             if player_two not in players_opponents[player_one]:
        #                 print('match after', player_one.__dict__.get('surname'), '//', player_two.__dict__.get('surname'))
        #                 players_current_round.append(player_one)
        #                 players_current_round.append(player_two)
        #                 f
                        
                    

                    


        









        
        # for i in range(0, len(self.players)-1):
        #     if self.players[i+1] in players_opponents[self.players[i]] :
        #         print('yes')        
        #         print(self.players[i+1].__dict__.get('surname'))
        #         print(self.players[i+1])
        #         print(players_opponents[self.players[i]])
        #         print(i)
        #     else:
        #         print('no')
        
        exit()
