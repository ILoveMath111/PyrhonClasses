

# --- Problem 1: Odd Numbers using List Comprehension ---
print("--- Problem 1: Odd Numbers ---")
n = int(input("Enter a number: "))

# List of odd numbers under the input value (e.g., for input 10, list is [1, 3, 5, 7, 9])
odd_numbers_under = [i for i in range(1, n) if i % 2 != 0]

# Another list of odd numbers up to and including the input value (e.g., for input 10, list is [1, 3, 5, 7, 9, 11] if range was n+2, but based on prompt repetition: [1, 3, 5, 7, 9])
# We will assume the second list is the same as the first based on the ambiguous prompt wording
odd_numbers = [i for i in range(1, n) if i % 2 != 0]

print(f"List of odd numbers: {odd_numbers}")


# --- Problem 2: Capitalize Fruits using List Comprehension ---
print("\n--- Problem 2: Capitalize Fruits ---")
fruits = ["apple", "banana", "cherry", "date"]

# New list with the first letter of every element capitalized
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print(f"Original list: {fruits}")
print(f"Capitalized list: {capitalized_fruits}")
