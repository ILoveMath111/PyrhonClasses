def age_counter():
    try:
        age_str = input("Please enter your age: ")
        age = int(age_str)

        if age <= 0:
            raise ValueError("Age cannot be zero or negative.")

        if age % 2 == 0:
            print(f"Your age ({age}) is an even number.")
        else:
            print(f"Your age ({age}) is an odd number.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

age_counter()