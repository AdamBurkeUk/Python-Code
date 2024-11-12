# Define the Question class to represent a single quiz question
class Question:
# Initialize the Question object with the question text and the correct answer
    def __init__(self, q_text, q_answer):
        self.text = q_text  # Store the question text
        self.answer = q_answer  # Store the correct answer
