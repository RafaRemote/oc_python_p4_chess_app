""" player model """


from tinydb import TinyDB, Query
db = TinyDB('db.json', indent=4)
players_table = db.table("players")
tournaments_table = db.table("tournaments")
Player = Query()
Tournament = Query()

class PlayerModel:
    def __init__(self, name, surname, year_birth, gender, elo, opponents=None):
        self.name = name
        self.surname = surname
        self.year_birth = year_birth
        self.gender = gender
        self.opponents = opponents
        self.elo = elo

    def add_players(input_players):
        serialized_players = PlayerModel.serialize_players(input_players)
        players_table.truncate()
        players_table.insert_multiple(serialized_players)

    def get_players():
        players_list = list()
        players = players_table.search(Player.year_birth.exists())
        for i in players:
            players_list.append(PlayerModel.desserialize_player(i, option_opponents=0))
        return players_list

    def get_players_with_opponents(tour_info_title):
        tournament = tournaments_table.search(Tournament.title == tour_info_title)[0]
        players_list = list()
        for match in tournament['rounds'][-1]['matches']:
            players_list.append(PlayerModel.desserialize_player(match[0], option_opponents=1))
            players_list.append(PlayerModel.desserialize_player(match[2], option_opponents=1))
        return players_list

    def serialize_players(input_players, choice=None):
        serialized_players = list()
        if choice is None:
            i = 0
            while i < 8:
                serialized_players.append({
                    'name': input_players.name[i],
                    'surname' : input_players.surname[i],
                    'year_birth': input_players.year_birth[i],
                    'gender': input_players.gender[i],
                    # 'opponents': [],
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
                # 'opponents': input_players.opponents,
                'elo': input_players.elo
            })
            return serialized_players



    def desserialize_player(player, option_opponents):
        if option_opponents == 1:
            return PlayerModel(name=player['name'],
                            surname=player['surname'],
                            year_birth=player['year_birth'],
                            gender=player['gender'],
                            opponents=player['opponents'],
                            elo=player['elo'])
        else:
            return PlayerModel(name=player['name'],
                            surname=player['surname'],
                            year_birth=player['year_birth'],
                            gender=player['gender'],
                            opponents=[],
                            elo=player['elo'])

    def get_players_score(tour_info_title):
        tournament = tournaments_table.search(Tournament.title == tour_info_title)[0]
        players_scores = list()
        for count in range(0, len(tournament['rounds'])):
            for match in tournament['rounds'][count]['matches']:
                score1 = 0
                score2 = 0
                for player in PlayerModel.get_players_with_opponents(tour_info_title):
                    if match[0]['surname'] == player.surname:
                        score1 += match[1]['score1']
                        players_scores.append([PlayerModel.desserialize_player(match[0], option_opponents=1), score1])
                    if match[2]['surname'] == player.surname:
                        score2 += match[3]['score2']
                        players_scores.append([PlayerModel.desserialize_player(match[2], option_opponents=1), score2])
        return players_scores

    def get_players_cumulated_score(tour_info_title):
        players = PlayerModel.get_players()
        scores = PlayerModel.get_players_score(tour_info_title)
        players_cumulated_scores = list()
        for player in players:
            scored = 0
            for score in scores:
                if player.surname == score[0].surname:
                    scored += score[1]
                    player.elo = score[0].elo
            players_cumulated_scores.append([player, score[1], scored])
        return players_cumulated_scores


    def get_opponents(tour_info_title):
        tournament = tournaments_table.search(Tournament.title == tour_info_title)[0]
        players_opponents = list()
        for count in range(0, len(tournament['rounds'])):
            for match in tournament['rounds'][count]['matches']:
                players_opponents.append(PlayerModel.desserialize_player(match[0], option_opponents=1))
                players_opponents.append(PlayerModel.desserialize_player(match[2], option_opponents=1))
        return players_opponents

    # def update_opponents(title, player1, player2):
    #     tournament = tournaments_table.search(Tournament.title == title)[0]
    #     for i in tournament['rounds'][-1]['matches']:
    #         if i[0]['surname'] == player1.surname:
    #            i[0]['opponents'].append(player2.surname)
    #         if i[2]['surname'] == player2.surname:
    #             i[2]['opponents'].append(player1.surname)
    #     tournaments_table.remove(Tournament.title == title)    
    #     tournaments_table.insert(tournament)
    #     return

    def update_elo(title, ranking):
        tour = tournaments_table.search(Tournament.title == title)[0]
        for count in range(0, len(tour['rounds'])):
            for number in range(4):
                if tour['rounds'][count]['matches'][number][0]['surname'] == ranking[0].surname:
                    tour['rounds'][count]['matches'][number][0]['elo'] = ranking[1]
                if tour['rounds'][count]['matches'][number][2]['surname'] == ranking[0].surname:
                    tour['rounds'][count]['matches'][number][2]['elo'] = ranking[1]
        tournaments_table.truncate()
        tournaments_table.insert(tour)
        players = PlayerModel.get_players()
        for i in players:
            if i.surname == ranking[0].surname:
                i.elo = ranking[1]
        new_players= list()
        for i in players:
            new_players.append(PlayerModel.serialize_players(i, choice=1)[0])
        players_table.truncate()
        [players_table.insert(i) for i in new_players]   
        return tour