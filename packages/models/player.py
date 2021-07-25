""" Player model """

from packages.views.input_player import InputPlayerView
from tinydb import TinyDB, Query
db = TinyDB('db.json', indent=4)
players_table = db.table("players")
tournaments_table = db.table("tournaments")
Player = Query()
Tournament = Query()


class PlayerModel:
    """
    Class for represent a player
    ...

    Attributes
    ----------
    name: str
        name
    surname: str
        surname
    year_birth: int
        year of birth
    gender: str
        man or woman
    elo: int
        elo

    Methods
    -------
    add_players(input_players, title):
        add a table of players in the database
    get_players(title):
        returns a list of players instances
    get_players_in_game(tour_info_title):
        returns a list of players instances currently playing
    serialize_players(input_players):
        return either a list or one serialized player object(s)
    get_elo(surname):
        returns the elo of a player in the players table
    desserialize_player(player):
        returns a player object from a serialized player object
    get_players_score(tour_info):
        returns a list of player instances with their score
    get_opponents(tour_info):
        returns a list of player instances with their opponents
    check_opponents(tour_info, player1, player2):
        returns boolean
        True if player2 already played with player1, otherwise False
    update_elo(tour_info, ranking):
        returns tournament instances with updated players elos
    """

    def __init__(self, name, surname, year_birth, gender, elo):
        """
        Constructs all the necessary attributes for the player object.

        Parameters
        ----------
        name: str
            name
        surname: str
            surname
        year_birth: int
            year of birth
        gender: str
            man or woman
        elo: int
            elo
        """

        self.name = name
        self.surname = surname
        self.year_birth = year_birth
        self.gender = gender
        self.elo = elo

    def add_players(input_players, title):
        """
        insert players to the database

        Parameters
        ----------
        input_players: list
            list of player instances
        title:
            tournament titie

        Returns
        -------
        none
        """

        serialized_players = PlayerModel.serialize_players(input_players)
        serialized_players.append({'tournament_participation': title})
        players_table.truncate()
        players_table.insert_multiple(serialized_players)

    def get_players(title):
        """
        get the players in the player table

        Parameters
        ----------
        title:
            tournament title

        Returns
        -------
        list of PlayerModel instances
        """

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
        """
        returns a list of players for a tournament

        Parameters
        ----------
        tour_info_title:
            tournament titie

        Returns
        -------
        list of PlaerModel instancs, can be empty
        """

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
        """
        serialize input for player


        Parameters
        ----------
        input_players: list
            list of player instances

        Returns
        -------
        either a list or one serialized player object
        """

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
        """
        check the elo of a player

        Parameters
        ----------
        surname: str
            surname of the player


        Returns
        -------
        int
        """

        player = players_table.search(Player.surname == surname)[0]
        return player['elo']

    def desserialize_player(player):
        """
        desserialized dict of player from the databse

        Parameters
        ----------
        player: dict
            dict representing player

        Returns
        -------
        instance of a player
        """

        return PlayerModel(name=player['name'],
                           surname=player['surname'],
                           year_birth=player['year_birth'],
                           gender=player['gender'],
                           elo=PlayerModel.get_elo(player['surname']))

    def get_players_score(tour_info):
        """
        get players scores

        Parameters
        ----------
        tour_info:
            tournament instance

        Returns
        -------
        list: [<player instance>, [score list], sum of scores list]
        """

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
        """
        get opponents for each player, only surnames of opponents

        Parameters
        ----------
        tour_info:
            tournament instance

        Returns
        -------
        list: within 8 times: [<player instance>, ['opponent(s)'s surname']]
        """

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
        """
        chek if two players did play together or not

        Parameters
        ----------
        tour_info: instance
            tournament instance
        player1: instance
            player instance
        player2:
            player instance

        Returns
        -------
        boolean: True if they played together False if not
        """

        players_opponents = PlayerModel.get_opponents(tour_info)
        for player in players_opponents:
            if player1.surname == player[0].surname:
                if player2.surname in player[1]:
                    return True
                else:
                    return False

    def update_elo(tour_info, ranking):
        """
        update elo of player in the database

        Parameters
        ----------
        tour_info: instance
            TournamentModel instance
        ranking:
            [<PlayerModel instance>, score]

        Returns
        -------
        TournamentModel instance
        """

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
