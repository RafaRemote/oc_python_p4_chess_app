def display_menu(one_dictionnary):
    print('Choose your option')
    print()
    counter = 0
    for i,j in one_dictionnary.items():
        counter += 1
        print(counter, '-', j)
