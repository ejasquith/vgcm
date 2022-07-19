"""
Create game objects to represent items in a user's collection.

Classes:
    Game
"""


class Game:
    """
    A class to represent a game.
    ----------
    Attributes
    ----------
    title : string
        title of the game
    publisher : string
        publisher of the game
    platform : string
        platform the game was released to
    """
    def __init__(self, title, publisher, platform):
        self.title = title
        self.publisher = publisher
        self.platform = platform
