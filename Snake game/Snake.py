from turtle import Turtle, Screen
import time
# Starting positions for the snake's segments
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
move_distance = 20 # Distance the snake moves in each step
UP = 90  # Direction for moving up
DOWN = 270  # Direction for moving down
LEFT = 180  # Direction for moving left
RIGHT = 0  # Direction for moving right


class Snake:
    def __init__(self):
        self.snakes = []  # List to store the snake's segments
        self.create_snake()  # Create the initial snake with starting positions
        self.head = self.snakes[0]  # Set the head of the snake as the first segment

    def create_snake(self):
        # Create the initial snake segments using the starting positions
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
# Create a new segment and add it to the snake
        new_snake = Turtle('square')  # Create a square-shaped segment
        new_snake.color('white')   # Set the color of the segment
        new_snake.penup()  # Prevent drawing lines when moving
        new_snake.goto(position)  # Position the segment at the given coordinates
        self.snakes.append(new_snake)  # Add the new segment to the snake

    def reset(self):
# Move all snake segments off-screen and reset the snake
        for snake in self.snakes:
            snake.goto(1000,1000)  # Move segments far off-screen
        self.snakes.clear()  # Clear the list of segments
        self.create_snake()  # Create a new snake
        self.head = self.snakes[0]   # Set the new head of the snake

    def extend(self):
# Add a new segment to the snake at the position of the last segment
        self.add_segment(self.snakes[-1].position())

    def move(self):
# Move the snake, starting from the tail to the head
        for snake_num in range(len(self.snakes) - 1, 0, -1):
# Move each segment to the position of the segment in front of it
            new_x = self.snakes[snake_num - 1].xcor()
            new_y = self.snakes[snake_num - 1].ycor()
            self.snakes[snake_num].goto(new_x, new_y)
# Move the head of the snake forward
        self.head.forward(move_distance)

    def up(self):
# Change the direction of the head to up, unless it's already moving down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
# Change the direction of the head to down, unless it's already moving up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
# Change the direction of the head to right, unless it's already moving left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
# Change the direction of the head to left, unless it's already moving right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

