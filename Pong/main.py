# Import the Screen class from the turtle module to create the game window
from turtle import  Screen

# Import the time module to control the frame rate and add delays in the game loop
import time

# Import the Paddle class from the Player module to create player-controlled paddles
from Player import Paddle

# Import the Ball class from the ball module to create and control the ball in the game
from ball import Ball

# Import the Score class from the score module to manage and display the game score
from score import Score

# Screen settings for the game
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("PONG")
screen.tracer(0)

# Create a paddle on the left side of the screen at position (-350, 0)
left_paddle = Paddle((-350,0))
# Create a paddle on the right side of the screen at position (350, 0)
right_paddle = Paddle((350,0))
# Initialize the ball at the center of the screen
ball = Ball()
# Initialize the score display for tracking each player's points
score = Score()

# Enable the screen to listen for keyboard input
screen.listen()

# Set up key bindings to control the right paddle:
# Pressing the "Up" arrow will call the right paddle's move_up method
screen.onkey(right_paddle.move_up,"Up")
# Pressing the "Down" arrow will call the right paddle's move_down method
screen.onkey(right_paddle.move_down,"Down")

# Set up key bindings to control the left paddle:
# Pressing the "w" key will call the left paddle's move_up method
screen.onkey(left_paddle.move_up, "w")
# Pressing the "s" key will call the left paddle's move_down method
screen.onkey(left_paddle.move_down, "s")

# Set the frame rate to 1/60th of a second (60 frames per second)
frame_rate = 1 / 60
# Flag to keep the game loop running
game_is_on = True
# Start the main game loop
while game_is_on:
# Pause the loop for the frame rate duration
    time.sleep(frame_rate)
# Refresh the screen to show the latest game state
    screen.update()
 # Move the ball in its current direction
    ball.move()

# Check if the ball hits the top or bottom of the screen
    if ball.ycor() > 290 or ball.ycor() < -290:
# Reverse the ball's vertical direction if it hits top or bottom
        ball.bounce_y()

# Check if the ball hits either paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < - 340:
# Reverse the ball's horizontal direction if it hits a paddle
        ball.bounce_x()

# Check if the ball goes out of bounds on the right side
    if ball.xcor() >= 380:
# Award a point to the left paddle and reset the ball position
        score.increase_left_paddle_scores()
        ball.refresh()

# Check if the ball goes out of bounds on the left side
    if ball.xcor() <= -380:
# Award a point to the right paddle and reset the ball position
        score.increase_right_paddle_scores()
        ball.refresh()

# Check if either player has reached 10 points to end the game
    if score.left_paddle_score == 10 or score.right_paddle_score == 10:
# End the game loop and display "Game Over"
        game_is_on = False
        score.game_over()


# Keep the game window open until the user clicks on it to close
screen.exitonclick()