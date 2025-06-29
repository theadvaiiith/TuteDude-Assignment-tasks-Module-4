import math

def calculate_math_operations(number):
    # Calculate square root, natural logarithm, and sine
    square_root = math.sqrt(number)
    natural_log = math.log(number)
    sine_value = math.sin(number)
    
    # Display results using f-strings
    print(f"\nResults for the number {number}:")
    print(f"Square root: {square_root}")
    print(f"Natural logarithm (ln): {natural_log}")
    print(f"Sine (in radians): {sine_value}")

# Main program: Get user input and call the function
try:
    number = float(input("Enter a number: "))
    calculate_math_operations(number)
except ValueError:
    print("Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {e}")
