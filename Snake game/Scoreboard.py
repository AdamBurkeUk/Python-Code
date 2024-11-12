from turtle import Turtle
ALIGNMENT = 'center'  # Alignment for the scoreboard text
FONT = ("Courier", 24, "normal")  # Font style for the scoreboard text

# Define the Scoreboard class as a subclass of Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()   # Initialize the Turtle class
        self.score = 0  # Initialize the current score to 0
# Read the high score from a file and store it as an integer
        with open("data.txt",mode= "r") as data:
            self.high_score = int(data.read())  # Set the high score from the file

        self.color("white")  # Set the color of the scoreboard text to white
        self.penup()  # Lift the pen to prevent drawing lines
        self.goto(0, 270)  # Position the scoreboard at the top center of the screen
        self.hideturtle()  # Hide the Turtle cursor
        self.update_scoreboard()   # Call method to display initial scoreboard

    def update_scoreboard(self):
        self.clear()  # Clear the previous scoreboard display
# Write the current score and high score on the screen
        self.write(f"Score:{self.score}  Highscore : {self.high_score}  ", align=ALIGNMENT, font=FONT)


    def increase_score(self):
            self.score += 1  # Increment the score by 1
            self.clear()  # Clear the old score
            self.update_scoreboard()  # Update the scoreboard with the new score


    def reset(self):
# If the current score exceeds the high score, update the high score
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as data:  # Write the new high score to the file
                data.write(f"{self.high_score}")
        self.score = 0  # Reset the current score
        self.update_scoreboard()  # Update the scoreboard to reflect the reset score