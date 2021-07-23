""" player model """
import time

from tinydb import TinyDB, Query
db = TinyDB('db.json', indent=4)
players_table = db.table("players")
tournaments_table = db.table("tournaments")
Player = Query()
Tournament = Query()


class PlayerModel:
    def __init__(self, name, surname, year_birth, gender, elo=None, opponents=None):
        self.name = name
        self.surname = surname
        self.year_birth = year_birth
        self.gender = gender
        self.opponents = opponents
        self.elo = self.get_elo()

    def get_elo(self):
        try:
            player = players_table.search(Player.surname == self.surname)[0]
            return player['elo']
        except IndexError:
            return

    def add_players(input_players, title):
        serialized_players = PlayerModel.serialize_players(input_players)
        serialized_players.append({'tournament_participation': title})
        players_table.truncate()
        players_table.insert_multiple(serialized_players)

    def get_players(title):
        players_list = []
        players = list()
        if len(players_table.search(Player.tournament_participation == title)) == 0:
            return players_list
        elif players_table.all()[-1]['tournament_participation'] == title:
            players = players_table.all()[0:8]
            for i in players:
                players_list.append(PlayerModel.desserialize_player(i, option_opponents=0))
            return players_list

    def get_players_in_game(tour_info_title):
        tournament = tournaments_table.search(Tournament.title == tour_info_title)[0]
        players_list = list()
        if len(tournament['rounds']) > 0:
            for match in tournament['rounds'][-1]['matches']:
                players_list.append(PlayerModel.desserialize_player(match[0], option_opponents=1))
                players_list.append(PlayerModel.desserialize_player(match[2], option_opponents=1))
            return players_list
        else:
            return []

    def serialize_players(input_players, choice=None):
        serialized_players = list()
        if choice is None:
            i = 0
            while i < 8:
                serialized_players.append({
                    'name': input_players.name[i],
                    'surname': input_players.surname[i],
                    'year_birth': input_players.year_birth[i],
                    'gender': input_players.gender[i],
                    'elo': input_players.elo[i]
                })
                i += 1
            return serialized_players
        else:
            serialized_players.append({
                'name': input_players.name,
                'surname': input_players.surname,
                'year_birth': input_players.year_birth,
                'gender': input_players.gender,
                'elo': input_players.elo
            })
            return serialized_players

    def desserialize_player(player, option_opponents):
        if option_opponents == 1:
            return PlayerModel(name=player['name'],
                               surname=player['surname'],
                               year_birth=player['year_birth'],
                               gender=player['gender'],
                               opponents=player['opponents'])
        else:
            return PlayerModel(name=player['name'],
                               surname=player['surname'],
                               year_birth=player['year_birth'],
                               gender=player['gender'],
                               opponents=[])

    def get_players_score(tour_info):
        rounds = tour_info.rounds
        print('dealing with this amount of rounds:')
        print(len(rounds))
        time.sleep(3)
        for i in range(0, len(rounds)):
            for j in range(4):
                print(rounds[i].matches[j].player1[0].surname)
        time.sleep(3)

        players = list()
        if len(rounds) > 0:
            [players.append([i, []]) for i in PlayerModel.get_players(tour_info.title)]
            for player in players:
                for round_number in range(0, len(rounds)):
                    for match in rounds[round_number].matches:
                        if player[0].surname == match.player1[0].surname:
                            player[1].append(match.player1[1])
                        if player[0].surname == match.player2[0].surname:
                            player[1].append(match.player2[1])
            [player.append(sum(player[1])) for player in players]
            print(players)
            time.sleep(3)
            return players
        else:
            [players.append([i, [0]] for i in PlayerModel.get_players(tour_info_title))]
            [player.append(sum(player[1])) for player in players]
            return players

    def get_opponents(tour_info_title):
        tournament = tournaments_table.search(Tournament.title == tour_info_title)[0]
        players_opponents = list()
        for count in range(0, len(tournament['rounds'])):
            for match in tournament['rounds'][count]['matches']:
                players_opponents.append(PlayerModel.desserialize_player(match[0], option_opponents=1))
                players_opponents.append(PlayerModel.desserialize_player(match[2], option_opponents=1))
        return players_opponents

    def update_elo(title, ranking):
        players = PlayerModel.get_players(title)
        for i in players:
            if i.surname == ranking[0].surname:
                i.elo = ranking[1]
        new_players = list()
        for i in players:
            new_players.append(PlayerModel.serialize_players(i, choice=1)[0])
        new_players.append({'tournament_participation': title})
        players_table.truncate()
        [players_table.insert(i) for i in new_players]
        return
