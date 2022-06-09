class Cast:
    """A collection of objects.

    The responsibility of a cast is to keep track of a collection of objects. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _objects (dict): A dictionary of objects (gem, rocks, and player)  { key: group_name, value: a list of objects }
    """

    def __init__(self):
        """Constructs a new objects."""
        self._objects = {}
        
    def add_objects(self, group, object):
        """Adds an object to the given group.
        
        Args:
            group (string): The name of the group.
            object (MovingObject): The object to add.
        """
        if not group in self._objects.keys():
            self._objects[group] = []
            
        if not object in self._objects[group]:
            self._objects[group].append(object)

    def get_objects(self, group):
        """Gets the objects in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The objects in the group.
        """
        results = []
        if group in self._objects.keys():
            results = self._objects[group].copy()
        return results
    
    def get_all_objects(self):
        """Gets all of the objects in the cast.
        
        Returns:
            List: All of the objects in the cast.
        """
        results = []
        for group in self._objects:
            results.extend(self._objects[group])
        return results

    def get_first_object(self, group):
        """Gets the first object in the given group.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            List: The first object in the group.
        """
        result = None
        if group in self._objects.keys():
            result = self._objects[group][0]
        return result

    def remove_object(self, group, object):
        """Removes an object from the given group.
        
        Args:
            group (string): The name of the group.
            object (MovingObject): The object to remove.
        """
        if group in self._objects:
            self._objects[group].remove(object)