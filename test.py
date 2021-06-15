# from packages.models.match import MatchModel
# from packages.models.player import PlayerModel

# from packages.models.round.RoundModel import RoundModel


# lst = [

#     PlayerModel(['Simpsons', 'Homer', 1980, 'm', 1000]),
#     PlayerModel(['Simpsons', 'Marge', 1985, 'm', 2000]),
#     PlayerModel(['Simpsons', 'Bart', 2010, 'm', 500]),
#     PlayerModel(['Simpsons', 'Lisa', 2011, 'm', 3000]),
#     PlayerModel(['Simpsons', 'Maggie', 2018, 'm', 1500]),
#     PlayerModel(['Nahasapee', 'Apu', 1970, 'm', 3000]),
#     PlayerModel(['Montgomery', 'Charles', 1900, 'm', 5000]),
#     PlayerModel(['Flanders', 'Ned', 1880, 'm', 2000])

# ]

# l = []
# for i in lst:
#     l.append(i.__dict__.get('elo'))
#     l.append(i)

# newlist = sorted(lst, key=lambda x: x.elo, reverse=True)

# high_group = newlist[:4]
# low_group = newlist[4:]

# matches = []


# for i in range(0, 4):
#     matches.append( MatchModel(high_group[i], low_group[i], score1=0, score2=0))

# for match in matches:
#     print(
#         match.__dict__.get('player1')[0].__dict__.get('surname'), 
#         match.__dict__.get('player1')[0].__dict__.get('elo'))
#     print(
#         match.__dict__.get('player2')[0].__dict__.get('surname'), 
#         match.__dict__.get('player2')[0].__dict__.get('elo'))
#     print()

# t = {'name': 'bib', 
#     'place': 'Paris', 
#     'date': 'Mon 14 June 2021', 
#     'total_rounds': 4
#     }
 

# print(t.get('name'))



# from termcolor import colored


# def check_score():
#     scores = [0, 0.5, 1]
#     scores_string = ['0', '0.5', '1']
#     while True:
#         score = input('score ?: ')
#         if score not in scores and score not in scores_string:
#             print(colored(f'{score} is not correct. You need to choose between: 0, 0.5 or 1', 'red'))
#             return input('score ?:' )
#         else:
#             return score



# # print(check_score())
# from packages.models.player import PlayerModel

# lst = [
#     {'1', (<packages.models.player.PlayerModel object at 0x109c5e460>, 0)}
#     {'0', (<packages.models.player.PlayerModel object at 0x109c5e400>, 0)}  
#     {'0.5', (<packages.models.player.PlayerModel object at 0x109c5e5e0>, 0)}
#     {'0.5', (<packages.models.player.PlayerModel object at 0x109c5e640>, 0)}
#     {(<packages.models.player.PlayerModel object at 0x109c5e4c0>, 0), '1'}
#     {'0', (<packages.models.player.PlayerModel object at 0x109c5e730>, 0)}
#     {(<packages.models.player.PlayerModel object at 0x109c5e6d0>, 0), '0'}
#     {(<packages.models.player.PlayerModel object at 0x109c5e6a0>, 0), '1'}

# ]


#3






# lst = [
#     [0,5000],
#     [1,2000],
#     [0,3000],
#     [1,1500],
#     [1,1000],
#     [1,4000],
#     [1,2000],
#     [0,500],
#     [0,100],
# ]

# import operator
# list1 = sorted(lst, key=operator.itemgetter(0, 1))
# list1.reverse()

# for i in range(8):
#     print(i)

    

# for i in range(0,8):
#     if i%2 == 0:
#         j = i

#         print(j,j+1)
#         3


# for i in range(4,8):
#     print(i)

