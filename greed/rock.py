#player looses a point
import random
from greed_classes.color import Color
from greed_classes.point import Point
from greed_classes.movingObject import MovingObject
#player earn a point

class Rock(MovingObject):
    """A falling object, if the Player tocuhes it, they will earn one point. 

    Attributes:
    
    """
    def __init__(self):
        """
        Constructs a new rock object.

        Args:
        self (Rock): An instance of MovingObject.
        """
        super().__init__()
        self._value = -1 

        self._character = 'o'  #dont do this here
        self._color = Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def get_value(self):
        return self._value