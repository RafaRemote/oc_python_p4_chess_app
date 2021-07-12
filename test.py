class Person:
    def __init__(self, name, age):
        self.name = name,
        self.age = age


jean = Person('jean', 23)
marc = Person('marc', 44)

lst = [jean, marc]


for i in lst:
    if i.__dict__['name'][0] == 'jean':
        print('yes')
        i == 0

print(lst)

