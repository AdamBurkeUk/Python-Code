from turtle import Turtle
import random  # Import random module for random choices

# Define constants for car properties
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]  # Car colors
STARTING_MOVE_DISTANCE = 5  # Initial movement speed for cars
MOVE_INCREMENT = 5  # Speed increment for each level up

class CarManager:
# Initialize the CarManager with attributes to store all car objects and set initial speed
    def __init__(self):
        self.all_cars = []  # List to hold all car instances
        self.car_speed = STARTING_MOVE_DISTANCE  # Initial speed of cars

# Method to create new car instances at random intervals
    def create_car(self):
        random_chance = random.randint(1,4)   # 25% chance to create a new car each call
        if random_chance == 1:
            new_car = Turtle('square')  # Create new turtle object representing the car
            new_car.shapesize(stretch_wid=1,stretch_len=2)  # Stretch to look like a car
            new_car.penup()  # Lift pen to avoid drawing lines
            new_car.color(random.choice(COLORS))  # Set a random color from COLORS
            random_y = random.randint(-250,250)   # Random y-position for car within screen bounds
            new_car.goto(300,random_y)   # Place car at starting x-position off the right edge of screen
            self.all_cars.append(new_car)  # Add new car to all_cars list

# Method to move each car in all_cars list to the left
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)  # Move car left by the current car_speed

# Method to increase speed of all cars when the player levels up
    def level_up(self):
        self.car_speed += MOVE_INCREMENT  # Increase car_speed by MOVE_INCREMENT


    pass
