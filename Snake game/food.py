from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle class to inherit its methods and attributes
        self.shape('circle')  # Set the shape of the food to a circle
        self.penup()  # Lift the pen to prevent drawing lines
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Set the size of the food
        self.color('blue')  # Set the color of the food
        self.speed('fastest')  # Set the food's movement speed to fastest
        random_x = random.randint(-270,270)  # Generate a random x-coordinate for placement
        random_y = random.randint(-270,270)  # Generate a random y-coordinate for placement
        self.goto(random_x,random_y)   # Position the food at the random coordinates
        self.refresh()   # Call refresh to reposition the food randomly

    def refresh(self):
# Generate new random coordinates for the food to reappear in a different location
        random_x = random.randint(-270, 270) # Generate a new random x-coordinate
        random_y = random.randint(-270, 270) # Generate a new random y-coordinate
        self.goto(random_x, random_y)  # Move the food to the new random position


