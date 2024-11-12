from turtle import Turtle, Screen   # Import necessary classes from the turtle module
import time  # Import time module to control the game speed
from Snake import Snake  # Import the Snake class (for the player's snake)
from food import Food  # Import the Food class (for the food object)
from Scoreboard import Scoreboard  # Import the Scoreboard class (for score tracking)

# Set up the game window
screen = Screen()
screen.setup(width=600, height=600)  # Set the dimensions of the game window
screen.bgcolor('black')  # Set the background color of the game window to black
screen.title("My Snake Game")  # Set the title of the game window
screen.tracer(0)  # Turn off automatic screen updates for manual control

# Create game objects
snake = Snake()  # Instantiate a new snake object
food = Food()  # Instantiate a new food object
scoreboard = Scoreboard()  # Instantiate a new scoreboard object

# Set up keyboard controls for the snake
screen.listen()   # Listen for keyboard inputs
screen.onkey(snake.up,"Up")  # Bind the "Up" key to move the snake up
screen.onkey(snake.down,"Down")  # Bind the "Down" key to move the snake down
screen.onkey(snake.left,"Left")  # Bind the "Left" key to move the snake left
screen.onkey(snake.right,"Right")  # Bind the "Right" key to move the snake right



# Start the game loop
game_is_on = True
while game_is_on:
    screen.update()  # Manually update the screen to avoid auto updates
    time.sleep(0.1)  # Control the speed of the game (lower values make the game faster)
    snake.move()  # Move the snake

# Check if the snake eats the food
    if snake.head.distance(food) < 15:  # If the snake's head is close to the food
        food.refresh()  # Reposition the food randomly
        snake.extend()  # Add a new segment to the snake
        scoreboard.increase_score()  # Increase the score

# Check if the snake hits the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()  # Reset the score if the snake hits the wall
        snake.reset()  # Reset the snake to its initial state

# Check if the snake collides with itself
    for snakes in snake.snakes[1:]:   # Check each segment of the snake except the head
        if snake == snake.head:   # Skip the head itself
            pass
        elif snake.head.distance(snakes) < 10:  # If the head collides with any other segment
            scoreboard.reset()  # Reset the score
            snake.reset()  # Reset the snake to its initial state

# Closes Game
screen.exitonclick()