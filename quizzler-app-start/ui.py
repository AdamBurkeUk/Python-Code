from tkinter import *
from quiz_brain import QuizBrain
# Define a constant for the theme color used in the interface
THEME_COLOR = "#375362"

# Define the QuizInterface class that handles the user interface for the quiz
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain  # Store the quiz logic object
        self.window = Tk()  # Create the main window for the quiz interface
        self.window.title("Quizzler")  # Set the window title
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)  # Set padding and background color for the window

 # Create a canvas to display the question text
        self.canvas = Canvas(width=300,height=250)  # Set canvas size
# Create text for the question on the canvas
        self.question_text = self.canvas.create_text(150,125,width=280,text="French",fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2)  # Position canvas on the grid layout

# Load the image for the "True" button and create the button with the corresponding command
        true_image = PhotoImage(file="images/true.png")  # Load image for True button
        self.true_button = self.button = Button(image=true_image,highlightthickness=0,command=self.true_pressed)  # Create True button
        self.button.grid(row=2,column=0)  # Position True button on the grid

# Load the image for the "False" button and create the button with the corresponding command
        false_image = PhotoImage(file="images/false.png")  # Load image for False button
        self.false_button = self.button = Button(image=false_image,highlightthickness=0,command=self.false_pressed)  # Create False button
        self.button.grid(row=2,column=1)  # Position False button on the grid

# Create a label to display the score and position it on the grid
        self.score_label = Label(text=f"Score: 0 ",bg=THEME_COLOR,font=("Arial",20,"bold"))  # Score label
        self.score_label.grid(row=0,column=1,pady=25)  # Position score label on the grid

        self.get_next_question()  # Get and display the next question

# Start the Tkinter event loop to run the quiz interface
        self.window.mainloop()

# Method to get and display the next question
    def get_next_question(self):
        self.canvas.config(bg='white')  # Reset canvas background color to white
        if self.quiz.still_has_questions():   # Check if there are more questions to display
            self.score_label.config(text=f"Score: {self.quiz.score}")  # Update the score label
            q_text = self.quiz.next_question()  # Get the next question text from the quiz logic
            self.canvas.itemconfig(self.question_text,text=q_text)  # Update the question text on the canvas
        else:   # If no more questions, display a completion message
            self.canvas.itemconfig(self.question_text,text="YOU HAVE FINISHED THE QUIZ")   # Display finish message
            self.true_button.config(state="disabled")  # Disable the True button
            self.false_button.config(state="disabled")  # Disable the False button

# Method called when the True button is pressed
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")  # Check if "True" is the correct answer
        self.give_feedback(is_right)  # Provide feedback based on the correctness of the answer

# Method called when the False button is pressed
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")  # Check if "False" is the correct answer
        self.give_feedback(is_right)  # Provide feedback based on the correctness of the answer

 # Method to give feedback based on whether the answer was correct or not
    def give_feedback(self,is_right):
        if is_right:  # If the answer was correct
            self.canvas.config(bg="green")  # Set canvas background to green for correct answer
            self.window.after(1000,self.get_next_question)   # Wait for 1 second before getting the next question
        else:
            self.canvas.config(bg="red")  # Set canvas background to red for incorrect answer
            self.window.after(1000,self.get_next_question)   # Wait for 1 second before getting the next question
