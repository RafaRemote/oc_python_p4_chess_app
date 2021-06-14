import os

def display_menu(one_dictionnary):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('   ', one_dictionnary['name'])
    print()
    print()
    counter = 0
    for i,j in one_dictionnary.items():
        if isinstance(j, list) and j[0] != one_dictionnary['name']:
            for k in j:
                print(counter + 1, '-', j[counter])
                counter += 1
    print()
                