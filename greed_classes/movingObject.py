import random
from greed_classes.color import Color
from greed_classes.point import Point

class MovingObject:
    """An object moving on the screen.
    
    Attributes:
            _character: the textual representation of the moving object.
            _font_size: The font size to use.
            _color (Color): The color of the object.
            _position: The vertical and horizontal position of the object (x,y)
            _velocity: The speed and direction.
    
    """
    def __init__(self):
        """
        Constructs a new object.

        Args:
        self (MovingObject): An instance of MovingObject.
        """
        self._character = ''
        self._font_size = 15
        self._color = Color(265,265,265)
        self._position = Point(0,0)
        self._velocity = Point(0, 0)


    def set_color(self, color):
        """Updates the color to the given one.
        
        Args:
            color (Color): The given color.
        """
        self._color = color

    def get_color(self):
        """Gets the object's color as a tuple of three ints (r, g, b).
        
        Returns:
            Color: The object's text color.
        """
        return self._color

    def set_character(self, text):
        """Updates the text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._character = text
    
    def set_font_size(self, font_size):
        """Sets the font size to the given value.
        
        Args:
            font_size (int): The given value.
        """
        self._font_size = font_size
    

    def get_text(self):
        """Returns its character.
        
        Args:
            text (string): The given value.
        """
        return self._character

    def get_font_size(self):
        """Gets the object's font size.
        
        Returns:
            Point: The object's font size.
        """
        return self._font_size

    def get_position(self):
        """Gets the object's position (x,y).
        
        Returns:
            Point: The object's position in the screen.
        """
        return self._position
    def get_character(self):
        """Gets the object's textual representation.
        
        Returns:
            string: The object's textual representation.
        """
        return self._character
    
    def set_position(self, position):
        """Updates the position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position
    
    def set_velocity(self, velocity):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity

    def get_velocity(self):
        """Gets the object's speed and direction.
        
        Returns:
            Point: The object's speed and direction.
        """
        return self._velocity
    def move_next(self, max_x, max_y):
        """Moves the object to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y())
        self._position = Point(x, y)
    
    def move_object(self, max_y):
        """Moves the object to its next position according to its velocity, from the top to the bottom.
        
        Args:
            max_y (int): The maximum y value.
        """
        print('moving') # to check if it is getting to this point
        x = self._position.get_x()
        dy = self._position.get_y()

        y = (dy + self._velocity.get_y()) % max_y

        if y > max_y:
            y = 0
        self._position = Point(x, y)
        self._velocity = self._position.scale(15)



    

        