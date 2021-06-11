""" entry point of the application"""

from packages.views.home import Home


if __name__ == "__main__":
    app = Home()
    app()