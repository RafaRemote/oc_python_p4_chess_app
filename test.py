{'tour_info': <packages.models.tournament.TournamentModel object at 0x10dc20a90>,
 'number': 2, 'players': [
        [
            <packages.models.player.PlayerModel object at 0x10e70bc70>, 
            <packages.models.player.PlayerModel object at 0x10e714850>, 
            <packages.models.player.PlayerModel object at 0x10dbf30a0>, 
            <packages.models.player.PlayerModel object at 0x10e70b430>, 
            <packages.models.player.PlayerModel object at 0x10dbf3040>, 
            <packages.models.player.PlayerModel object at 0x10e70be80>, 
            <packages.models.player.PlayerModel object at 0x10dc23cd0>, 
            <packages.models.player.PlayerModel object at 0x10e7147c0>]], 
            'start_date': '20/06/2021, 09:06:10', 
            'end_date': None, 
            'next_matches': [<packages.models.match.MatchModel object at 0x10e7067f0>, <packages.models.match.MatchModel object at 0x10e706280>, <packages.models.match.MatchModel object at 0x10e7062e0>, <packages.models.match.MatchModel object at 0x10e706610>], 'matches': [[<packages.models.match.MatchModel object at 0x10e7067f0>, <packages.models.match.MatchModel object at 0x10e706280>, <packages.models.match.MatchModel object at 0x10e7062e0>, <packages.models.match.MatchModel object at 0x10e706610>]]}



update = TournamentModel.update_tour(   round.tour_info,
                                round.players,
                                round.number,
                                round.start_date,
                                round.end_date,
                                round.matches
                            )

{'tour_title': 'r', 
'tour_time_control': 'rapid', 
'tour_description': 'e', 
'start_date': '20/06/2021, 09:18:29', 
'place': 'Paris', 
'total_rounds': 4, 
'rounds': [
    [1, '20/06/2021, 09:18:35', '20/06/2021, 09:18:48', [<packages.models.match.MatchModel object at 0x10c73b790>, <packages.models.match.MatchModel object at 0x10c73be20>, <packages.models.match.MatchModel object at 0x10c73bcd0>, <packages.models.match.MatchModel object at 0x10c73bee0>]], 
    [2, '20/06/2021, 09:18:50', None, [[<packages.models.match.MatchModel object at 0x10c73b700>, <packages.models.match.MatchModel object at 0x10c73bac0>, <packages.models.match.MatchModel object at 0x10c73b5e0>, <packages.models.match.MatchModel object at 0x10c73bf10>]]]], 
    'players': [[<packages.models.player.PlayerModel object at 0x10c73adf0>, <packages.models.player.PlayerModel object at 0x10c73aa90>, <packages.models.player.PlayerModel object at 0x10c73af10>, <packages.models.player.PlayerModel object at 0x10c73abe0>, <packages.models.player.PlayerModel object at 0x10c73aee0>, <packages.models.player.PlayerModel object at 0x10c73a7f0>, <packages.models.player.PlayerModel object at 0x10bc22040>, <packages.models.player.PlayerModel object at 0x10c73ab50>]


{'tour_title': 'r', 
'tour_time_control': 
'rapid', 
'tour_description': 'e', 'start_date': '20/06/2021, 09:18:29', 'place': 'Paris', 'total_rounds': 4, 
'rounds': [[1, '20/06/2021, 09:18:35', '20/06/2021, 09:18:48', [<packages.models.match.MatchModel object at 0x10c73b790>, <packages.models.match.MatchModel object at 0x10c73be20>, <packages.models.match.MatchModel object at 0x10c73bcd0>, <packages.models.match.MatchModel object at 0x10c73bee0>]], 
[2, '20/06/2021, 09:18:50', '20/06/2021, 09:20:00', [<packages.models.match.MatchModel object at 0x10c73b760>, <packages.models.match.MatchModel object at 0x10c73b0d0>, <packages.models.match.MatchModel object at 0x10c73bfa0>, <packages.models.match.MatchModel object at 0x10c73ba00>]], 
[3, '20/06/2021, 09:20:05', None, [[<packages.models.match.MatchModel object at 0x10c73b7f0>, <packages.models.match.MatchModel object at 0x10c73bf10>, <packages.models.match.MatchModel object at 0x10c73b430>, <packages.models.match.MatchModel object at 0x10c73bbb0>]]]], 
'players': [[<packages.models.player.PlayerModel object at 0x10c73adf0>, <packages.models.player.PlayerModel object at 0x10c73aa90>, <packages.models.player.PlayerModel object at 0x10c73af10>, <packages.models.player.PlayerModel object at 0x10c73abe0>, <packages.models.player.PlayerModel object at 0x10c73aee0>, <packages.models.player.PlayerModel object at 0x10c73a7f0>, <packages.models.player.PlayerModel object at 0x10bc22040>, <packages.models.player.PlayerModel object at 0x10c73ab50>]]}


tu créeun fichier setup.cfg et tu met [flake8]
exclude =
    .git,
    __pycache__,
    env/
max-line-length = 119