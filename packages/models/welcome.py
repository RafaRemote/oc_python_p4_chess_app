""" welcome model """

title = 'Welcome'
sub_title = 'to your chess tournament app'


class WelcomeModel:
    def __init__(self):
        self.title = title
        self.sub_title = sub_title

    def __call__(self):
        return self
