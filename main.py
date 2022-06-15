# Gems (*) and rocks (o) randomly appear and fall from the top of the screen.
# The player (#) can move left or right along the bottom of the screen.
# If the player touches a gem they earn a point.
# If the player touches a rock they lose a point.
# Gems and rocks are removed when the player touches them.
# The game continues until the player closes the window.


import random
from greed_classes.player import Player
from greed_classes.rock import Rock
from greed_classes.gem import Gem
from greed_classes.director import Director
from greed_classes.keyboard_service import KeyboardService
from greed_classes.video_service import VideoService
from greed_classes.color import Color
from greed_classes.point import Point
from greed_classes.cast import Cast


FRAME_RATE = 12
MAX_X = 1000
MAX_Y = 800
CELL_SIZE = 15
FONT_SIZE = 22
COLS = 60
ROWS = 40
CAPTION = "Greed Game"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 50


def main():
    cast = Cast()
    player = Player()
    player.set_character("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    position = Point((MAX_X//2),(MAX_Y-20))
    player.set_position(position)
    cast.add_objects("players", player)
    
    for i in range(DEFAULT_ARTIFACTS):
        x = random.randint(0, COLS)
        y = MAX_Y
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        random_number = random.randint(0,10)
        if (random_number % 2) == 0:  
            object = Rock()  
            object.set_character('o')
            group = 'movingObjects'
        else:
            object = Gem()  
            object.set_character('*')
            group = 'movingObjects'
        velocity = Point(0,-1)
        object.set_velocity(velocity)
        object.set_font_size(FONT_SIZE)
        object.set_color(color)
        object.set_position(position)
        cast.add_objects(group, object)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()