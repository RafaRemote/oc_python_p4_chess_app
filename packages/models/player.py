""" player model """


# from test import Tournament
from tinydb import TinyDB, Query
db = TinyDB('db.json')

import json

Player = Query()

class PlayerModel:
    def __init__(self, name, surname, year_birth, gender, elo, score=0.0):
        self.name = name
        self.surname = surname
        self.year_birth = year_birth
        self.gender = gender
        self.opponents = list()
        self.elo = elo
        self.score = score
        self.unique_id = self.surname + str(self.elo)

    def add_opponent(self, opponent):
        self.opponents.append(opponent)

    def update_player_score(player):
        if player is not None:
            players = db.search(Player.players.exists())[0]['players']
            for person in players:
                if person['surname'] == player['surname']:
                    person['score'] = player['score']
            db.update({'players': players}, Player.players.exists())
        else: 
            return
    
    def __call__(self):
        return self
