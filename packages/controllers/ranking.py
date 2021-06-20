""" dcostrings """

from packages.views.ranking import RankingView


class RankingController:
    def __init__(self, tour_info):
        self.tour_info = tour_info
        self.players = None

    def __call__(self):
        self.players = [i for i in self.tour_info.__dict__['players'][0]]
        self.players.sort(key=lambda x: x.score, reverse=True)
        show_details = RankingView(self.players)
        show_details()
