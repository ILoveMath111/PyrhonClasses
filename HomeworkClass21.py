def square_it_out(start_range, end_range):
    # Create an empty list to store the square values
    squared_values = []
    # Create empty lists to store the odd and even squared values
    odd_squares = []
    even_squares = []

    # Iterate through the specified range (inclusive of start and exclusive of end+1 for range() behavior)
    for number in range(start_range, end_range + 1):
        # Calculate the square of the number
        square = number ** 2
        # Append the square to the main list
        squared_values.append(square)

        # Check if the square is even or odd using the modulus operator
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)

    return squared_values, odd_squares, even_squares
