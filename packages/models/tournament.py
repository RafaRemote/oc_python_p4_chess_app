""" model tournament """

import datetime

from packages.models.round import RoundModel
from packages.models.player import PlayerModel
from packages.views.error import Error
from packages.models.match import MatchModel

from tinydb import TinyDB, Query

db = TinyDB('db.json', indent=4)
Tournament = Query()
tournaments_table = db.table('tournaments')

TOTALROUNDS = 4


class TournamentModel:
    def __init__(self, place, title, time_control, description, start_date, rounds=[]):
        self.place = place
        self.title = title
        self.time_control = time_control
        self.description = description
        self.start_date = start_date
        self.total_rounds = TOTALROUNDS
        self.rounds = rounds

    def insert(self):
        if len(tournaments_table.search(Tournament.title == self.title)) == 0:
            tournaments_table.insert({'place': self.place,
                                      'title': self.title,
                                      'time_control': self.time_control,
                                      'description': self.description,
                                      'start_date': datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
                                      'rounds': self.rounds
                                      })
        else:
            error = Error(f'Tournament \' {self.title} \' already exists, you can\'t add it again')
            error()
            return

    def get_tournament(title):
        tour_db = tournaments_table.search(Tournament.title == title)[0]
        tour = TournamentModel(place=tour_db['place'],
                               title=tour_db['title'],
                               time_control=tour_db['time_control'],
                               description=tour_db['description'],
                               start_date=tour_db['start_date'],
                               rounds=TournamentModel.deserialize_rounds(tour_db))
        return tour

    def get_tournament_by_id(choice):
        tour_db = tournaments_table.get(doc_id=choice)
        tour = TournamentModel(place=tour_db['place'],
                               title=tour_db['title'],
                               time_control=tour_db['time_control'],
                               description=tour_db['description'],
                               start_date=tour_db['start_date'],
                               rounds=TournamentModel.deserialize_rounds(tour_db))
        return tour

    def deserialize_rounds(tour_db):
        rounds_list = list()
        matches_list = list()
        rounds = tour_db['rounds']
        numbers = list()
        start_dates = list()
        end_dates = list()
        if len(rounds) == 0:
            return []
        else:
            for i in rounds:
                if len(i['matches']) > 0:
                    for j in range(4):
                        matches_list.append(MatchModel(
                            player1=PlayerModel(i['matches'][j][0]['name'],
                                                i['matches'][j][0]['surname'],
                                                i['matches'][j][0]['year_birth'],
                                                i['matches'][j][0]['gender'],
                                                i['matches'][j][0]['elo'],
                                                i['matches'][j][0]['opponents']),
                            player2=PlayerModel(i['matches'][j][2]['name'],
                                                i['matches'][j][2]['surname'],
                                                i['matches'][j][2]['year_birth'],
                                                i['matches'][j][2]['gender'],
                                                i['matches'][j][2]['elo'],
                                                i['matches'][j][2]['opponents']),
                                            score1=i['matches'][j][1]['score1'],
                                            score2=i['matches'][j][3]['score2']
                                            ))
                numbers.append(i['number'])
                start_dates.append(i['start_date'])
                end_dates.append(i['end_date'])
                while len(numbers) > 0:
                    for i in range(len(numbers)):
                        rounds_list.append(RoundModel(
                            matches=matches_list[:4],
                            number=numbers[0],
                            start_date=start_dates[0],
                            end_date=end_dates[0]
                        ))
                        del matches_list[:4]
                        del numbers[0]
                        del start_dates[0]
                        del end_dates[0]
        return rounds_list

    def deserialize_players(tour_db):
        players = tour_db['players']
        desserialized_players = list()
        for i in players:
            desserialized_players.append(PlayerModel(i['name'],
                                                     i['surname'],
                                                     i['year_birth'],
                                                     i['gender'],
                                                     i['elo'],
                                                     i['opponents']
                                                     ))
        return desserialized_players

    def get_all_tournaments():
        listing = tournaments_table.search(Tournament.title.exists())
        sorted_listing = sorted(listing, key=lambda x: x['title'])
        return [TournamentModel.get_tournament(i['title']) for i in sorted_listing]

    def get_all_tournaments_db_doc():
        """ Returns the list of tournaments from the db, containing the doc_id.
            Will be useful for the View tournaments.
            List sorted by doc_id
        """
        return sorted(tournaments_table.search(Tournament.title.exists()), key=lambda x: x.doc_id)

    def get_rounds_length(tour):
        tournament = tournaments_table.search(Tournament.title == tour.title)[0]
        return len(tournament['rounds'])

    def add_first_round_db(tour_info):
        players = PlayerModel.get_players(tour_info.title)
        players_elo_sorted = sorted(players, key=lambda x: x.elo, reverse=True)
        high_group = players_elo_sorted[:4]
        low_group = players_elo_sorted[4:]
        matches = []
        for i in range(0, len(high_group)):
            matches.append([{
                                "name": high_group[i].name,
                                "surname": high_group[i].surname,
                                "year_birth": high_group[i].year_birth,
                                "gender": high_group[i].gender,
                                "elo": high_group[i].elo,
                                "opponents": [low_group[i].surname]
                            },
                            {
                                "score1": 0
                            },
                            {
                                "name": low_group[i].name,
                                "surname": low_group[i].surname,
                                "year_birth": low_group[i].year_birth,
                                "gender": low_group[i].gender,
                                "elo": low_group[i].elo,
                                "opponents": [high_group[i].surname]
                            },
                            {
                                "score2": 0
                            }
                            ])
            round = [{'matches': matches,
                      'number': 1,
                      'start_date': str(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")),
                      'end_date': ''
                      }]
            tournaments_table.update({'rounds': round}, Tournament.title == tour_info.title)

    def add_round(tour_info, matches):
        tour = tournaments_table.search(Tournament.title == tour_info.title)[0]
        round = dict()
        round['matches'] = list()
        for i in matches:
            round['matches'].append([
                                    {
                                        "name": i.player1[0].name,
                                        "surname":i.player1[0].surname,
                                        "year_birth":i.player1[0].year_birth,
                                        "gender":i.player1[0].gender,
                                        "elo":i.player1[0].elo,
                                        "opponents":i.player1[0].opponents
                                    },
                                    {
                                        "score1": 0
                                    },
                                    {
                                        "name": i.player2[0].name,
                                        "surname":i.player2[0].surname,
                                        "year_birth":i.player2[0].year_birth,
                                        "gender":i.player2[0].gender,
                                        "elo":i.player2[0].elo,
                                        "opponents":i.player2[0].opponents
                                    },
                                    {
                                        "score2": 0
                                    }
                                    ])
        round['number'] = len(tour['rounds'])+1
        round['start_date'] = str(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
        round['end_date'] = ""
        tour['rounds'].append(round)
        tournaments_table.remove(Tournament.title == tour_info.title)
        tournaments_table.insert(tour)
        return

    def update_scores(tour_info, scores):
        tour = tournaments_table.search(Tournament.title == tour_info.title)[0]
        for i in scores:
            for j in tour['rounds'][-1]['matches']:
                if i[0].surname == j[0]['surname']:
                    j[1]['score1'] = i[2]
                if i[1].surname == j[2]['surname']:
                    j[3]['score2'] = i[3]
        tour['rounds'][-1]['end_date'] = str(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
        tournaments_table.remove(Tournament.title == tour_info.title)
        tournaments_table.insert(tour)

    def __call__(self):
        self.insert()
        return self
