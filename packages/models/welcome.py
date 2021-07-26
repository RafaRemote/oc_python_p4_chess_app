""" Welcome model """

title = 'Welcome'
sub_title = 'to your chess tournament app'


class WelcomeModel:
    """
    Class to represent the welcome page
    ...

    Attributes
    ----------
    title: str
        string displayed as a title
    subtitle: str
        message under the title

    Methods
    -------
    call(self):
        returns attributes for a WelcomeModel instance

    """

    def __init__(self):
        """
        Constructs attributes for WelcomeModel object.

        Parameters
        ----------
        none

        """

        self.title = title
        self.sub_title = sub_title

    def __call__(self):
        """ returns WelcomeModel instance """

        return self
