import time  # Import time module for adding delays in the game loop
from turtle import Screen  # Import Screen class to set up the game screen
from player import Player  # Import custom Player class to handle player functionality
from car_manager import CarManager   # Import custom CarManager class to manage car objects
from scoreboard import Scoreboard   # Import custom Scoreboard class to display and manage the score

# Set up screen dimensions and basic settings
screen = Screen()
screen.setup(width=600, height=600)  # Set screen size to 600x600 pixels
screen.tracer(0)  # Turn off-screen auto-updating for smoother animations

# Create instances of the main game object
player = Player()  # Instantiate the player object
car_manager = CarManager()  # Instantiate the car manager to control cars
scoreboard = Scoreboard()  # Instantiate the scoreboard to track the player's level

# Set up key bindings for player movement
screen.listen()  # Listen for key presses
screen.onkey(player.move_up,"Up")  # Move player up when "Up" key is pressed
screen.onkey(player.move_down,'Down')  # Move player down when "Down" key is pressed

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Delay each game loop iteration for a smoother experience
    screen.update()  # Update the screen to reflect the latest game state

# Create and move cars across the screen
    car_manager.create_car()  # Randomly create new cars
    car_manager.move_cars()  # Move all cars to the left

# Check for collision between player and car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:   # If a car is close to the player, trigger game over
            scoreboard.game_over()  # Display "Game Over" message
            game_is_on = False  # End the game loop

# Check if player has reached the finish line
    if player.is_at_finsh():
        player.go_to_start()  # Reset player position to the start
        car_manager.level_up()  # Increase car speed to make the game harder
        scoreboard.increase_level()  # Increase level and update the display

# Exit game screen on click
screen.exitonclick()
