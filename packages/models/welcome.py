""" welcome model """

welcome_message = 'Welcome'
welcome_sub_title = 'to your chess tournament app'


class WelcomeModel:
    def __init__(self):
        self.message = welcome_message
        self.sub_title = welcome_sub_title

    def __call__(self):
        return self
