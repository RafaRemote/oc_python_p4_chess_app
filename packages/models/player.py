""" player model """

from packages.views.input_player import InputPlayerView
from tinydb import TinyDB, Query
db = TinyDB('db.json', indent=4)
players_table = db.table("players")
tournaments_table = db.table("tournaments")
Player = Query()
Tournament = Query()


class PlayerModel:
    def __init__(self, name, surname, year_birth, gender, elo):
        self.name = name
        self.surname = surname
        self.year_birth = year_birth
        self.gender = gender
        self.elo = elo

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
                players_list.append(PlayerModel.desserialize_player(i))
            return players_list

    def get_players_in_game(tour_info_title):
        tournament = tournaments_table.search(Tournament.title == tour_info_title)[0]
        players_list = list()
        if len(tournament['rounds']) > 0:
            for match in tournament['rounds'][-1]['matches']:
                players_list.append(PlayerModel.desserialize_player(match[0]))
                players_list.append(PlayerModel.desserialize_player(match[2]))
            return players_list
        else:
            return []

    def serialize_players(input_players):
        if isinstance(input_players, InputPlayerView):           
            serialized_players = list()
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
            return {
                'name': input_players.name,
                'surname': input_players.surname,
                'year_birth': input_players.year_birth,
                'gender': input_players.gender,
                'elo': input_players.elo
                }

    def get_elo(surname):
        player = players_table.search(Player.surname == surname)[0]
        return player['elo']

    def desserialize_player(player):
            return PlayerModel(name=player['name'],
                               surname=player['surname'],
                               year_birth=player['year_birth'],
                               gender=player['gender'],
                               elo=PlayerModel.get_elo(player['surname']))

    def get_players_score(tour_info):
        rounds = tour_info.rounds
        players = list()
        if len(rounds) > 0:
            [players.append([i, []]) for i in PlayerModel.get_players_in_game(tour_info.title)]
            for player in players:
                for round_number in range(0, len(rounds)):
                    for match in rounds[round_number].matches:
                        if player[0].surname == match.player1[0].surname:
                            player[1].append(match.player1[1])
                        if player[0].surname == match.player2[0].surname:
                            player[1].append(match.player2[1])
            [player.append(sum(player[1])) for player in players]
            return players
        else:
            [players.append([i, [0]]) for i in PlayerModel.get_players(tour_info.title)]
            [player.append(sum(player[1])) for player in players]
            return players

    def get_opponents(tour_info):
        players = list()
        [players.append([player, []]) for player in PlayerModel.get_players(tour_info.title)]
        for player in players:
            for round_n in range(0, len(tour_info.rounds)):
                for match_n in range(4):
                    if player[0].surname == tour_info.rounds[round_n].matches[match_n].player1[0].surname:
                        player[1].append(tour_info.rounds[round_n].matches[match_n].player2[0].surname)
                    if player[0].surname == tour_info.rounds[round_n].matches[match_n].player2[0].surname:
                        player[1].append(tour_info.rounds[round_n].matches[match_n].player1[0].surname)
        return players

    def check_opponents(tour_info, player1, player2):
        players_opponents = PlayerModel.get_opponents(tour_info)
        for player in players_opponents:
            if player1.surname == player[0].surname:
                if player2.surname in player[1]:
                    return True
                else:
                    return False

    def update_elo(tour_info, ranking):
        players = PlayerModel.get_players(tour_info.title)
        new_players = list()
        for i in players:
            new_players.append(PlayerModel.serialize_players(i))
        for player in new_players:
            if ranking[0].surname == player['surname']:
                player['elo'] = ranking[1]
        new_players.append({'tournament_participation': tour_info.title})
        players_table.truncate()
        [players_table.insert(i) for i in new_players]
        return tour_info
