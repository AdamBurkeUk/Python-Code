from turtle import Turtle

# Initialize scores for both paddles (left and right)
left_paddle_score = 0
right_paddle_score = 0

# Define the Score class that will handle score tracking and display
class Score(Turtle):
    def __init__(self):
# Initialize the Score class by calling the parent Turtle class's constructor
        super().__init__()
# Set initial scores to 0 for both paddles
        self.left_paddle_score = 0
        self.right_paddle_score = 0
# Set the score display color to white
        self.color("white")
# Lift the pen to prevent drawing lines while moving the turtle
        self.penup()
# Hide the turtle cursor (so it's invisible on the screen)
        self.hideturtle()
# Position the score display slightly below the top of the screen
        self.goto(0, 270)
# Move the turtle to the specific position for displaying the left paddle score
        self.goto(-100,200)
# Call the update_score method to display the initial scores
        self.update_score()

# Update the score display on the screen
    def update_score(self):
# Clear any existing score display to prepare for the updated score
        self.clear()
# Display the left paddle's score on the left side of the screen
        self.goto(-100, 200)
        self.write(self.left_paddle_score, align='center', font=('Courier', 80, 'normal'))
# Display the right paddle's score on the right side of the screen
        self.goto(100, 200)
        self.write(self.right_paddle_score, align='center', font=('Courier', 80, 'normal'))

# Increase the score of the left paddle by 1 and update the score display
    def increase_left_paddle_scores(self):
            self.left_paddle_score += 1  # Increment the left paddle score by 1
            self.clear()  # Clear the current score display
            self.update_score()  # Update the display with the new score

# Increase the score of the right paddle by 1 and update the score display
    def increase_right_paddle_scores(self):
            self.right_paddle_score += 1  # Increment the right paddle score by 1
            self.clear()  # Clear the current score display
            self.update_score()  # Update the display with the new score

# Display "GAME OVER" when the game ends
    def game_over(self):
            self.goto(0,0)   # Move the turtle to the center of the screen
            self.write("GAME OVER",align='center')  # Display the "GAME OVER" message in the center


