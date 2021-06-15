import datetime
import operator


TOTALROUNDS = 4
PLACE = 'Paris'

update_start_date = datetime.datetime.now().strftime("%a %d %B %Y")

ranking = []
sorted_ranking = []
class TournamentModel:
    def __init__(self, name, time_control, description, date=None):
        self.name = name
        self.time_control = time_control
        self.description = description
        self.start_date = date
        self.place = PLACE
        self.total_rounds = TOTALROUNDS
        self.rounds = []

    def __call__(self):
        return self

    # def add_round(self, instance_of_round):
    #     tournament_list[0].__dict__.get('rounds').append(instance_of_round)
    #     return(tournament_list[0])

    # def update_round(self, results):       
    #     for i in range(0,16):
    #         if i%2 == 0:
    #             j = i
    #             elo = results[j][0].__dict__.get('elo')
    #             ranking.append([results[j][0],results[j+1], elo])
    #     sorted_ranking = sorted(ranking, key=operator.itemgetter(1, 2))
    #     sorted_ranking.reverse()
    #     # for i in sorted_ranking:
    #     #     print(i)
    #     return [tournament_list, sorted_ranking]

   

            

                # if self.time_control is not None and self.time_control not in choice_of_times:
                #     return ['error', self.__class__.__name__, f'{self.time_control} does not match with the propositions']
                # else: 
                #     self.time_control = self.time_control
                # tournament_list.append(self)
                # return self

            # def add_round(self, round):
            #     self.rounds.append(round)

