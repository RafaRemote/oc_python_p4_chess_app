welcome_message = 'Welcome to your chess tournament manager!'


class WelcomeModel:
    def __init__(self):
        self.message = welcome_message

    def __call__(self):
        return self