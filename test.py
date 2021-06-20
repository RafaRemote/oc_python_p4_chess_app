from os import name


class Man:
    def __init__(self, name):
        self.name = name
        self.friends = []



jean = Man('jean')
bernard = Man('bernard')
marc = Man('marc')
paul = Man('paul')




class Man:
    def __init__(self, name):
        self.name = name
        self.opponents = []


jean = Man('jean')
bernard = Man('bernard')
luc = Man('luc')
marc = Man('marc')



men = [jean, bernard, marc, luc]

for man in men:
    while len(men) != 0:
        try:
            i = 0
            guy = men[0]
            oppo = men[i+1]
        
            if oppo not in guy.opponents:
                guy.opponents.append(oppo)
            else:
                del men[i+1]
                i += 1
        except IndexError:
            break

oppo_jean = []
print([oppo_jean.append(i.name) for i in jean.opponents])
# [print(i.name) for i in bernard.opponents]
# [print(i.name) for i in marc.opponents]
# [print(i.name) for i in luc.opponents]
[print(i.name) for i in jean.opponents]
[print(i.name) for i in bernard.opponents]
[print(i.name) for i in marc.opponents]
[print(i.name) for i in luc.opponents]