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
    
    def get_score(self):
        return self._score
    
    def add_point(self, point):
        self._score += point
        

    

