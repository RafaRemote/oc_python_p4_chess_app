""" entry point of the application"""

from packages.views.start import StartMenu


if __name__ == "__main__":
    app = StartMenu()
    app.welcome()
    app()