def get_choice(name, choice=None):
    choice = input('your choice: ')
    print(['i got', name, choice])
    return [name, choice]
