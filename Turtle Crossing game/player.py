from turtle import Turtle   # Import the Turtle class from the turtle module for graphics

# Constants for player positioning and movement
STARTING_POSITION = (0, -280)   # Starting position at the bottom center of the screen
MOVE_DISTANCE = 10  # Distance the player moves per key press
FINISH_LINE_Y = 280  # Y-coordinate that represents the finish line

class Player(Turtle):
# Initialize the Player as a Turtle object with specific attributes
    def __init__(self):
        super().__init__()   # Initialize the Turtle superclass
        self.shape('turtle')   # Set the player shape to a turtle
        self.color('red')  # Set the player color to red
        self.penup()  # Lift the pen to avoid drawing lines
        self.go_to_start()  # Start the player at the starting position
        self.setheading(90)   # Face the player upwards (90 degrees)

# Method to move the player up by a predefined distance
    def move_up(self):
        self.forward(MOVE_DISTANCE)  # Move the player forward (up) by MOVE_DISTANCE

# Method to move the player down by a predefined distance
    def move_down(self):
        self.backward(MOVE_DISTANCE)  # Move the player backward (down) by MOVE_DISTANCE

# Method to reset the player to the starting position
    def go_to_start(self):
        self.goto(STARTING_POSITION)  # Move the player to the starting position at the bottom

# Method to check if the player has reached the finish line
    def is_at_finsh(self):
        if self.ycor() > FINISH_LINE_Y:  # If the player's y-coordinate is past the finish line
            return True   # Player has reached the finish line
        else:
            return False  # Player has not yet reached the finish line