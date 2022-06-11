class Color:
    """A color.

    The responsibility of Color is to hold and provide information about itself inside a tuple.

    Attributes:
        _red (int): The red value.
        _green (int): The green value.
        _blue (int): The blue value.
        _alpha (int): The alpha or opacity.
    """
    
    def __init__(self, red, green, blue, alpha = 255):
        """Constructs a new Color using the specified red, green, and blue.
        
        Args:
            red (int): A red value.
            green (int): A green value.
            blue (int): A blue value.
            alpha (int): An alpha or opacity.
        """
        self._red = red
        self._green = green
        self._blue = blue 
        self._alpha = alpha

    def to_tuple(self):
        """Gets the color as a tuple of three values (red, green, and blue).

        Returns:
            Tuple(int, int, int): The color as a tuple.
        """
        return (self._red, self._green, self._blue, self._alpha)   