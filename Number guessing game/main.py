import random  # Import random module to generate a random number
from art import logo  # Import a logo from the art module to display at the start of the game

# Initialize global variables
numbers = list(range(0, 101 ,1))  # List of numbers from 0 to 100
guessing_num = 0  # Placeholder for the randomly selected number
attempts = 0  # Placeholder for the number of attempts based on difficulty

# Function to select a random number by shuffling the list and picking the last number
def random_num():
    global guessing_num
    random.shuffle(numbers)   # Shuffle the list to randomize the order
    guessing_num = numbers.pop()  # Assign the last element as the number to guess

# Function to set the difficulty level and the corresponding number of attempts
def guess_difficulty():
    global attempts
    while True:
        difficulty = str(input("Difficulty: Easy or Hard ")).lower()  # Get difficulty from user
        if difficulty == 'easy' :
            attempts = 10  # Set attempts to 10 for easy difficulty
            break
        elif difficulty == 'hard' :
            attempts = 5  # Set attempts to 5 for hard difficulty
            break
        else:
            print("pick a valid option")  # Error message if input is invalid

# Function to handle the guessing logic
def guesses():
    while True:
        try:
            global attempts
            guess = int(input("Make a guess: "))  # Prompt user to guess
            if guess == guessing_num:
                print(f"Guess Correct you win! the number was {guessing_num}")
                return  # End the function if the guess is correct
            elif guess > guessing_num:
                attempts -=1  # Decrement attempts
                print("wrong try again!")
                print("too high!")  # Hint if guess is too high
            elif guess < guessing_num:
                attempts -=1  # Decrement attempts
                print("wrong try again!")
                print("too low!")  # Hint if guess is too low

                # Check remaining attempts
                if attempts > 0:
                    print(f"you have {attempts} attempts left")  # Display attempts left
                elif attempts == 0:
                    print(f"you have ran out of attempts! you lose. the number was {guessing_num}.")
                    return  # End the function if no attempts are left
        except ValueError:
                print("please enter a valid number")  # Error message if input is not a number
                continue  # Prompt user to enter a valid number again




# Main function to start the game
def game_on():
    print(logo)  # Display the logo at the start
    print("Welcome to the guessing game")
    print("Im thinking of a number between 1-100")
    guess_difficulty()  # Set the difficulty level and number of attempts
    random_num()  # Select a random number to guess
    guesses()  # Start the guessing loop
# Call the main function to run the game
game_on()