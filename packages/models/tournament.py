""" model tournament """

from typing import Match
from tinydb import TinyDB, Query
from tinydb.table import Document
db = TinyDB('db.json')
Tournament = Query()

import datetime

from packages.models.player import PlayerModel
from packages.models.match import MatchModel

TOTALROUNDS = 4

tournaments_list = list()

class TournamentModel:
    def __init__(self, place, tour_title, tour_time_control, tour_description, tour_start_date, rounds=[], players=[]):
        self.place = place
        self.tour_title = tour_title
        self.tour_time_control = tour_time_control
        self.tour_description = tour_description
        self.tour_start_date = tour_start_date
        self.total_rounds = TOTALROUNDS
        self.rounds = rounds
        self.players = players

    def insert(self):
        db.insert({'place': self.place,
                   'tour_title': self.tour_title,
                   'tour_time_control': self.tour_time_control,
                   'tour_description': self.tour_description,
                   'tour_start_date': datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
                   'rounds': self.rounds,
                   'players': self.players}
                    )
        return self

    def search(self):
        if db.search(Tournament.tour_title == self.tour_title):
            tour = db.search(Tournament.tour_title == self.tour_title)
            tournament =  TournamentModel(place=tour[0]['place'],
                                   tour_title=tour[0]['tour_title'],
                                   tour_time_control=tour[0]['tour_time_control'],
                                   tour_description=tour[0]['tour_description'],
                                   tour_start_date=tour[0]['tour_start_date'],
                                   rounds=tour[0]['rounds'],
                                   players=tour[0]['players'])
            tournaments_list.append(tournament)
        else:
            print('Did not find a tournament with this name', self.tour_title)
            
    def update_tour_list(self):
        db_list = db.search(Tournament.tour_title.exists())
        obj_round = list()
        matches = list()
        for tour in db_list:
            tour_dico = dict(tour)
            round = tour_dico.get('rounds')
            if len(round) == 0:
                break
            else:
                for j in range(4):
                    matches.append(MatchModel(PlayerModel(round['matches'][j][0]['name'],
                                                            round['matches'][j][0]['surname'],
                                                            round['matches'][j][0]['year_birth'],
                                                            round['matches'][j][0]['gender'],
                                                            round['matches'][j][0]['elo'],
                                                            round['matches'][j][0]['score']),
                                PlayerModel(round['matches'][j][1]['name'],
                                            round['matches'][j][1]['surname'],
                                            round['matches'][j][1]['year_birth'],
                                            round['matches'][j][1]['gender'],
                                            round['matches'][j][1]['elo'],
                                            round['matches'][j][1]['score']))
                        )


        # players = [i['players'] for i in db_list]
        # obj_players = self.deserialize_players(players)
        [tournaments_list.append(i) for i in db_list if i not in tournaments_list]
        return tournaments_list

    def deserialize_players(players):
        pass

    def add_players(tour_info, serialized_players):
        db.update({'players': serialized_players} , Tournament.tour_title == tour_info['tour_title'])
        for i in serialized_players:
            tour_info['players'].append(PlayerModel(i['name'], 
                                                    i['surname'], 
                                                    i['year_birth'],
                                                    i['gender'],
                                                    i['elo'],
                                                    i['score']))
        return tour_info

    def get_players():
        return db.search(Tournament.players.exists())[0]['players']

    def add_first_round_db(tour_info):
        players = tour_info['players']
        players_elo_sorted = sorted(players, key=lambda x: x['elo'], reverse=True)
        high_group = players_elo_sorted[:4]
        low_group = players_elo_sorted[4:]
        matches = []
        for i in range(0, len(high_group)):
            matches.append([{"name": high_group[i]['name'],
                             "surname": high_group[i]['surname'],
                             "year_birth": high_group[i]['year_birth'],
                             "gender": high_group[i]['gender'],
                             "elo": high_group[i]['elo'],
                             "score" : high_group[i]['score']
                            },
                             {"name": low_group[i]['name'],
                              "surname": low_group[i]['surname'],
                              "year_birth": low_group[i]['year_birth'],
                              "gender": low_group[i]['gender'],
                              "elo": low_group[i]['elo'],
                              "score": low_group[i]['score']
                             }
                            ])
        round = {'matches': matches, 
                 'number': 1,
                 'start_date': str(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")),
                 'end_date': ''
        }
        db.update({'rounds': round}, Tournament['tour_title'] == tour_info['tour_title'])
    
    def __call__(self):
        self.insert()
        self.search()
        return self
