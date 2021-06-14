from packages.models.match import MatchModel
from packages.models.player import PlayerModel


lst = [

    PlayerModel(['Simpsons', 'Homer', 1980, 'm', 1000]),
    PlayerModel(['Simpsons', 'Marge', 1985, 'm', 2000]),
    PlayerModel(['Simpsons', 'Bart', 2010, 'm', 500]),
    PlayerModel(['Simpsons', 'Lisa', 2011, 'm', 3000]),
    PlayerModel(['Simpsons', 'Maggie', 2018, 'm', 1500]),
    PlayerModel(['Nahasapee', 'Apu', 1970, 'm', 3000]),
    PlayerModel(['Montgomery', 'Charles', 1900, 'm', 5000]),
    PlayerModel(['Flanders', 'Ned', 1880, 'm', 2000])

]

l = []
for i in lst:
    l.append(i.__dict__.get('elo'))
    l.append(i)

newlist = sorted(lst, key=lambda x: x.elo, reverse=True)

high_group = newlist[:4]
low_group = newlist[4:]

matches = []


for i in range(0, 4):
    matches.append( MatchModel(high_group[i], low_group[i], score1=0, score2=0))

for match in matches:
    print(
        match.__dict__.get('player1')[0].__dict__.get('surname'), 
        match.__dict__.get('player1')[0].__dict__.get('elo'))
    print(
        match.__dict__.get('player2')[0].__dict__.get('surname'), 
        match.__dict__.get('player2')[0].__dict__.get('elo'))
    print()







