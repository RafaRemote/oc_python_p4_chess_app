""" entry point of the application"""

from packages.views.home import HomeMenu


if __name__ == "__main__":
    app = HomeMenu()
    app.welcome()
    app()
