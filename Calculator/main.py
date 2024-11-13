from art import logo  # Import a logo design from the art module to display at the start of the program

# Define basic arithmetic functions for the calculator
def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

# Dictionary to map operation symbols to their respective functions
operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide
              }

# Main calculator function that prompts user for input and handles calculations
def calculator():
    print(logo)   # Display logo at the start of the program
    print('welcome to the calculator')
    calc_on = True  # Flag to keep calculator running
    first_number = float(input("first number?: "))  # Prompt for the first number

# Main loop for continuous calculations
    while calc_on:

# Display available operations
        for symbol in operations:
            print(symbol)
# Get the operation symbol from the user
            operation_symbol = input("operation?:")
# Validate operation input
            if operation_symbol not in operations:
                print("invalid operation please try again")
                continue   # Restart loop if the operation is invalid

# Prompt for the second number and execute calculation
            second_number = float(input("second number?:"))
            calculation_function = operations[operation_symbol]  # Select function based on operation symbol
            result = calculation_function(first_number,second_number)  # Calculate result
            print(f"{first_number} {operation_symbol} {second_number} = {result} ")

# Prompt user to continue or start new calculation
            go_again = input(f"type 'y' if you want to continue calculating with {result}, 'n' to start a new calculation").lower()
# Continue with the current result as the first number
            if go_again == 'y':
                first_number = result
            elif go_again == 'n':
                calculator()   # Restart the calculator for a new calculation
            else:
                print("invalid input, exiting calculator.")
                calc_on = False   # Exit the loop if input is invalid

# Start the calculator
calculator()