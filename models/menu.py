class MenuModel:
    def __init__(self, *args):
        i = 0
        for j in args:
            i += 1
            self.__dict__['option_' + str(i)] = j

    def __call__(self):
        for i in self:
            print(i)