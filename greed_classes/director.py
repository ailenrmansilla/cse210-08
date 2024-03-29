class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast all the moving objects.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):  
        """Gets directional input from the keyboard and applies it to the object to move it.
        
        Args:
            cast (Cast): The cast of the objects.
        """
        player = cast.get_first_object("players")  
        velocity = self._keyboard_service.get_direction()  #only moves to the right or to the left
        player.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the player's position and resolves any collisions with gems or rocks.
        
        Args:
            cast (Cast): The cast of objects.
        """
        
        player = cast.get_first_object("players")
        fallingObjects = cast.get_objects("movingObjects") # gems and rocks 
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)

        for object in fallingObjects:
            self._video_service.print_score(player) #call the video service and print the score on top
            object.move_object(max_y)
            if player.get_position().equals(object.get_position()): 
                player.add_point(object.get_value()) # add a point (negative or positive point, rock or gem value) to the player's score
                cast.remove_object('movingObjects',object)#remove the touched element
                
                   
        
    def _do_outputs(self, cast):
        """Draws the objects on the screen.
        
        Args:
            cast (Cast): The cast of all objects.
        """
        self._video_service.clear_buffer()
        objects = cast.get_all_objects()
        self._video_service.draw_movingObjects(objects)
        self._video_service.flush_buffer()