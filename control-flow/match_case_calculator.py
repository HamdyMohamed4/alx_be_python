# match_case_calculator.py

# Function to perform the calculation based on the selected operation
def calculator(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 == 0:
                return "Cannot divide by zero."
            else:
                return num1 / num2
        case _:
            return "Invalid operation."

# Prompt for user input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ")

    # Perform the calculation and display the result
    result = calculator(num1, num2, operation)
    print(f"The result is {result}.")
except ValueError:
    print("Please enter valid numbers.")
