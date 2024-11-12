from turtle import Turtle

# Define constants for the up and down directions (90 degrees for up, 270 degrees for down)
UP = 90
DOWN = 270

# Define the Paddle class, which is a subclass of the Turtle class
class Paddle(Turtle):
    def __init__(self,position):
# Initialize the Paddle class by calling the parent Turtle class's constructor
        super().__init__()
# Set the paddle's shape to a square
        self.shape('square')
# Set the paddle's color to white
        self.color('white')
# Stretch the paddle shape to make it rectangular (6 units high, 1 unit wide)
        self.shapesize(stretch_wid=6, stretch_len=1)
# Lift the pen so it doesn't leave a trail when moving
        self.penup()
# Position the paddle at the specified location (position passed as argument)
        self.goto(position)
# Define the speed at which the paddle moves
        self.paddle_speed = 40

# Move the paddle up by paddle_speed units, if it doesn't go beyond the top boundary
    def move_up(self):
        new_y = self.ycor() + self.paddle_speed  # Use the paddle_speed variable to control the movement
        if new_y < 250:  # Check if the new position is within the screen's upper limit
            self.goto(self.xcor(), new_y)  # Move the paddle to the new y position

# Move the paddle down by paddle_speed units, if it doesn't go beyond the bottom boundary
    def move_down(self):
        new_y = self.ycor() - self.paddle_speed   # Use the paddle_speed variable to control the movement
        if new_y > - 250:  # Check if the new position is within the screen's lower limit
            self.goto(self.xcor(),new_y)  # Move the paddle to the new y position