import math

# Get input from the user
try:
    number = float(input("Enter a number to find its square root: "))

    # Check for negative numbers
    if number < 0:
        print("Cannot calculate the square root of a negative number.")
    else:
        # Calculate the square root
        square_root = math.sqrt(number)

        # Display the result
        print(f"The square root of {number} is: {square_root}")

except ValueError:
    print("Invalid input. Please enter a valid number.")