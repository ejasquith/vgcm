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
    genre : string
        genre of the game
    publisher : string
        publisher of the game
    platform : string
        platform the game was released to
    release_date : datetime
        Date of the game's release     
    """
    def __init__(self, title, genre, publisher,
                 platform, release_date, ):
        self.title = title
        self.genre = genre
        self.publisher = publisher
        self.platform = platform
        self.release_date = release_date

    def listify(self):
        """
        Returns the object's properties as a list.
        """
        return [self.title, self.genre, self.publisher, self.platform,
                self.release_date.strftime("%d/%m/%Y")]
