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
    developer : string
        developer of the game
    platform : string
        platform the game was released to
    release_date : datetime
        Date of the game's release
    purchase_date : datetime
        Date the game was purchased        
    """
    def __init__(self, title, genre, publisher, developer,
                 platform, release_date, purchase_date):
        self.title = title
        self.genre = genre
        self.publisher = publisher
        self.developer = developer
        self.platform = platform
        self.release_date = release_date
        self.purchase_date = purchase_date

    def listify(self):
        """
        Returns the objects properties as a list.
        """
        return [self.title, self.genre, self.publisher,
                self.developer, self.platform,
                self.release_date.strftime("%d/%m/%Y"),
                self.purchase_date.strftime("%d/%m/%Y")]
