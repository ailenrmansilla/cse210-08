from greed_classes.color import Color
from greed_classes.movingObject import MovingObject

class Player(MovingObject):
    """A player who seeks to gather as many falling gems as possible.
    Attributes:
    Score(int): how many points they have
    """
    def __init__(self):
        """
        Constructs a new player.

        Args:
        self (player): An instance of moving Object.
        
        Attributes:
            _score: the total points.
            """
        super().__init__()
        self._score = 0 

    def set_score(self,score):
        """Sets the player's score.
        Args:
            Score(int): The player's initial score.
        """
        self._score = score
    def get_score(self):
        """Gets the player's score as a integer.
        
        Returns:
            _score: The player's score as a integer.
        """
        return self._score
    
    def add_point(self, point):
        self._score += point
        

    

