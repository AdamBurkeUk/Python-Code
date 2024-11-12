import requests  # Import the requests module to make HTTP requests


# Define the parameters for the API request:
# - amount specifies the number of questions to fetch (10 questions)
# - type specifies the type of questions (boolean, true/false questions)
parameters = {
    "amount": 10,
    "type": "boolean",

}

# Send a GET request to the trivia API with the specified parameters
question = requests.get(url="https://opentdb.com/api.php",params=parameters)
# Raise an exception if the request returns an error (non-2xx status code)
question.raise_for_status()
# Parse the response JSON data
data = question.json()
# Extract the 'results' key from the JSON response, which contains the trivia questions
question_data = data['results']

