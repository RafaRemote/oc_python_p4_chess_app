import datetime
from time import strftime

from packages.models.match import MatchModel 

player_1_opponents = []
player_2_opponents = []
player_3_opponents = []
player_4_opponents = []
player_5_opponents = []
player_6_opponents = []
player_7_opponents = []
player_8_opponents = []
class RoundModel:
    def __init__(self, tournament_name, players):
        self.tournmanent_name = tournament_name
        self.name = None
        self.start_date = None
        self.end_date = None
        self.matches = []
        self.players = players

    def round1(self):
        self.name = 'Round1'
        self.start_date = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        list_of_players = self.players[:8]
        cleaned_list = []
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
        # for i in obj_ranking:
        #     print(i[0])
        matches_round2 = []
        # for i in range(0,8):
        #     if i%2 == 0:
        #         j = i
        #         matches_round2.append(MatchModel(obj_ranking[j][0], obj_ranking[j+1][0], score1=0, score2=0))
        # for i in matches_round2:
        #     print(i.__dict__.get('player1')[0].__dict__.get('surname'), i.__dict__.get('player2')[0].__dict__.get('surname'))
        # for i in obj_round1:
        #     print(i.__dict__.get('player1')[0].__dict__.get('surname'), i.__dict__.get('player2')[0].__dict__.get('surname'))
        # for i in matches_round2:
        #     if i in obj_round1:
        #         print('found')
        #         print(i.__dict__.get('player1')[0].__dict__.get('surname'), i.__dict__.get('player2')[0].__dict__.get('surname'))
        #     else: 
        #         print('not found')
        #         print(i)
        #         print(i.__dict__.get('player1')[0].__dict__.get('surname'), i.__dict__.get('player2')[0].__dict__.get('surname'))
        for i in range(len(obj_ranking)):
                eval('player_' + str(i+1) + '_opponents').append(obj_ranking[i][0])

        for i in update:
            print(obj_round1)
        
        for j in obj_round1:
            for i in range(len(obj_round1)):
                if j.__dict__.get('player1')[0] in eval('player_' + str(i+1) + '_opponents'):
                    eval('player_' + str(i+1) + '_opponents').append(j.__dict__.get('player2')[0])
        
        for j in obj_round1:
            for i in range(len(obj_round1)):
                if j.__dict__.get('player2')[0] in eval('player_' + str(i+1) + '_opponents'):
                    eval('player_' + str(i+1) + '_opponents').append(j.__dict__.get('player1')[0])
        
                
            

        print(player_1_opponents[0].__dict__.get('surname'), len(player_1_opponents))
        print(player_2_opponents[0].__dict__.get('surname'), len(player_2_opponents))
        print(player_3_opponents[0].__dict__.get('surname'), len(player_3_opponents))
        print(player_4_opponents[0].__dict__.get('surname'), len(player_4_opponents))
        print(player_5_opponents[0].__dict__.get('surname'), len(player_5_opponents))
        print(player_6_opponents[0].__dict__.get('surname'), len(player_6_opponents))
        print(player_7_opponents[0].__dict__.get('surname'), len(player_7_opponents))
        print(player_8_opponents[0].__dict__.get('surname'), len(player_8_opponents))




        # print(player_1_opponents[0].__dict__.get('surname'))
        # print(player_2_opponents[0].__dict__.get('surname'))
        # print(player_3_opponents[0].__dict__.get('surname'))
        # print(player_4_opponents[0].__dict__.get('surname'))
        # print(player_5_opponents[0].__dict__.get('surname'))
        # print(player_6_opponents[0].__dict__.get('surname'))
        # print(player_7_opponents[0].__dict__.get('surname'))
        # print(player_8_opponents[0].__dict__.get('surname'))



        # print(obj_round1)
        # print(obj_ranking)

        exit()

