from turtle import Turtle

# Initial positions for the snake body segments
# These positions define the starting length and direction of the snake
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# Distance the snake moves forward on each step
MOVE_DISTANCE = 20

# Direction constants (in degrees) to improve readability
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    """
    The Snake class is responsible for creating and controlling
    the snake body, including movement and direction changes.
    """

    def __init__(self):
        super().__init__()

        # Stores all snake body segments as Turtle objects
        self.segments = []

        # Create the initial snake body
        self.create_snake()

        # The head is always the first segment
        # This makes direction and movement logic clearer
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the initial snake using predefined starting positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Adds a new segment to the snake at the given position.
        Each segment is a square turtle with no drawing trail.
        """
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        """
        Moves the snake forward by shifting each segment
        to the position of the segment in front of it.
        The head then moves forward by MOVE_DISTANCE.
        """
        # Move from the tail towards the head
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # Move the head forward in the current direction
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Turn the snake upward, unless it is currently moving down."""
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        """Turn the snake downward, unless it is currently moving up."""
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        """Turn the snake left, unless it is currently moving right."""
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        """Turn the snake right, unless it is currently moving left."""
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
