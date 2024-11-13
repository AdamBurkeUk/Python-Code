from turtle import Turtle

# Define the font style for scoreboard text
FONT = ("Courier", 24, "normal")   # Font type, size, and style for displaying text

class Scoreboard(Turtle):
# Initialize the scoreboard with a starting level and set up the display
    def __init__(self):
        super().__init__()  # Initialize the parent Turtle class
        self.level = 1  # Starting level is 1
        self.hideturtle()   # Hide the default turtle shape (since it's not needed for the scoreboard)
        self.penup()  # Lift the pen to prevent drawing lines
        self.goto(-280,260)  # Position the scoreboard text in the top left corner
        self.update_scoreboard()  # Update the scoreboard display

# Method to update the scoreboard by displaying the current level
    def update_scoreboard(self):
        self.clear()  # Clear previous scoreboard text

# Write the current level on the screen, aligned to the left, with the specified font
        self.write(f'Level:{self.level}', align='left', font=FONT)

# Method to increase the level by 1 and update the display
    def increase_level(self):
        self.level += 1  # Increment the level by 1
        self.update_scoreboard()  # Update the scoreboard to show the new level

# Method to display the "GAME OVER" message when the game ends
    def game_over(self):
        self.goto(0,0)  # Move the cursor to the center of the screen

# Write the "GAME OVER" message in the center of the screen with the specified font
        self.write('GAME OVER',align='center',font=FONT)
