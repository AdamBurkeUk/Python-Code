from turtle import Turtle

# The ball class is a turtle in the shape of a circle, that uses the functions below to move
class Ball(Turtle):
    def __init__(self):
# Initialize the Ball class as a subclass of Turtle
        super().__init__()
# Set the shape of the ball to a circle
        self.shape('circle')
# Lift the pen to prevent drawing lines while moving the ball
        self.penup()
# Set the ball's size (default size with stretch factor of 1)
        self.shapesize(stretch_len=1, stretch_wid=1)
# Set the color of the ball to white
        self.color('white')
# Set the ball's movement speed to a fast animation setting
        self.speed('fast')
# Position the ball at the center of the screen at the start
        self.goto(0,0)
# Set initial movement increments for the ball in both x and y directions
        self.x_move = 5
        self.y_move = 5
# Set the initial movement speed (controls time delay in game loop)
        self.move_speed = 0.5

# Move the ball to a new position based on its current direction
    def move(self):
        new_x = self.xcor() + self.x_move  # Calculate new x-coordinate
        new_y = self.ycor() + self.y_move  # Calculate new y-coordinate
        self.goto(new_x, new_y)  # Move ball to the new position

# Reverse the ball's vertical movement direction (bounce off top/bottom walls)
    def bounce_y(self):
        self.y_move *= -1  # Invert y-axis movement direction

# Reverse the ball's horizontal movement direction (bounce off paddles)
# and increase its speed slightly for added challenge
    def bounce_x(self):
        self.x_move *= -1  # Invert x-axis movement direction
        self.move_speed *= 0.5 # Increase ball speed by reducing delay factor

# Reset the ball to the center and reverse its direction after a point is scored
    def refresh(self):
        self.goto(0,0)  # Move ball back to the center
        self.bounce_x()  # Reverse ball's direction to change serve side
        self.move_speed = 0.5  # Reset the speed of the ball for the next round
