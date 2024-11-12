from question_model import Question  # Import the Question class to create question objects
from quiz_brain import QuizBrain  # Import the QuizBrain class to manage quiz logic
from data import question_data  # Import the data containing the questions for the quiz
from ui import QuizInterface  # Import the QuizInterface class to handle the user interface

# Create an empty list to store the question objects
question_bank = []
# Loop through the data and create Question objects for each trivia question
for question in question_data:
    question_text = question["question"]  # Extract the question text
    question_answer = question["correct_answer"]   # Extract the correct answer
    new_question = Question(question_text, question_answer)  # Create a new Question object
    question_bank.append(new_question)  # Add the question object to the question bank


# Create a QuizBrain object to manage quiz flow and scoring
quiz = QuizBrain(question_bank)
# Create the user interface for the quiz
quiz_ui = QuizInterface(quiz)

# The while loop is commented out, but its purpose would be to continue the quiz until all questions are answered
#while quiz.still_has_questions():
   # quiz.next_question()


# Print a message indicating the quiz is complete
print("You've completed the quiz")
# Print the user's final score out of the total questions answered
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
