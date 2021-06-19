""" docstrings """

TOTALROUNDS = 4
PLACE = 'Paris'
class TournamentModel:
    def __init__(self, tour_title, tour_time_control, tour_description, tour_start_date):
        self.tour_title = tour_title
        self.tour_time_control = tour_time_control
        self.tour_description = tour_description
        self.start_date = tour_start_date
        self.place = PLACE
        self.total_rounds = TOTALROUNDS
        self.rounds = list()
        self.players = list()


    def update_tour(tour_info, players, round_number, round_start_date, round_end_date, round_matches):
        round = [round_number, round_start_date, round_end_date, round_matches]
        tour_info.rounds.append(round)
        if len(tour_info.players) == 0:
            tour_info.players.append(players)
        return tour_info

    def update_tour_round(tour_info, round_number, round_start_date, round_end_date, round_matches):
        round = [round_number, round_start_date, round_end_date, round_matches]
        del tour_info.__dict__['rounds'][round_number-1]
        tour_info.__dict__['rounds'].append(round)
        return tour_info

    def __call__(self):
        return self
