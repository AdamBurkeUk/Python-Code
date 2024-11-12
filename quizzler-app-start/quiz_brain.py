# Import the html module to handle special character encoding in questions
import html
# Define the QuizBrain class that manages the quiz logic
class QuizBrain:

# Initialize the QuizBrain object with a list of questions
    def __init__(self, q_list):
        self.question_number = 0  # Initialize the question number to track which question is being asked
        self.score = 0  # Initialize the score to 0
        self.question_list = q_list  # Store the list of questions provided as input
        self.current_question = None   # Initialize a variable to hold the current question object

# Check if there are still more questions to ask in the quiz
    def still_has_questions(self):
        return self.question_number < len(self.question_list)  # Return True if more questions are available

# Move to the next question and return its text
    def next_question(self):
        self.current_question = self.question_list[self.question_number]  # Get the current question from the list
        self.question_number += 1   # Increment the question number
        q_text = html.unescape(self.current_question.text)  # Decode any HTML entities in the question text (e.g., "&quot;" becomes a quote)
        return f"Q.{self.question_number}: {q_text}"  # Return the formatted question text

#Check if the user's answer is correct
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer  # Get the correct answer for the current question
        if user_answer.lower() == correct_answer.lower():  # Compare the user answer to the correct answer (case-insensitive)
            self.score += 1  # Increment the score if the answer is correct
            return True  # Return True if the answer is correct
        else:
            return False  # Return False if the answer is incorrect


