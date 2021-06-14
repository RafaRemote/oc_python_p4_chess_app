class PlayerModel:
    def __init__(self, lst):    
        self.name = lst[0]
        self.surname = lst[1]
        self.year_of_birth = lst[2]
        self.gender = lst[3]
        self.elo = lst[4]

    def __call__(self):
        return self



PlayerModel(['Simpsons', 'Homer', 1980, 'm', 1000])
PlayerModel(['Simpsons', 'Marge', 1985, 'm', 2000])
PlayerModel(['Simpsons', 'Bart', 2010, 'm', 500])
PlayerModel(['Simpsons', 'Lisa', 2011, 'm', 3000])
PlayerModel(['Simpsons', 'Maggie', 2018, 'm', 1500])
PlayerModel(['Nahasapee', 'Apu', 1970, 'm', 3000])
PlayerModel(['Montgomery', 'Charles', 1900, 'm', 5000])
PlayerModel(['Flanders', 'Ned', 1880, 'm', 2000])


list = ['Simpsons', 'Homer', 1980, 'm', 1000, 'Simpsons', 'Marge', 1985, 'm', 2000, 'Simpsons', 'Bart', 2010, 'm', 500, 'Simpsons', 'Lisa', 2011, 'm', 3000, 'Simpsons', 'Maggie', 2018, 'm', 1500,'Nahasapee', 'Apu', 1970, 'm', 3000, 'Montgomery', 'Charles', 1900, 'm', 5000, 'Flanders', 'Ned', 1880, 'm', 2000]

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
