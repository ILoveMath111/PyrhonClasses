def clothing_advisor():
    """
    Advises Rohan on what to wear based on the current temperature.
    """
    # Ask Rohan for the temperature in Celsius
    try:
        current_temp = float(input("Hello Rohan! Please enter the current temperature in Celsius: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Define temperature ranges for different clothing types
    # These are general guidelines; Rohan can adjust them for his comfort.
    if current_temp > 25:
        print("The weather is warm. It's the perfect time to wear light and soft clothes!")
    elif 15 <= current_temp <= 25:
        print("The temperature is mild. A long-sleeve shirt or a light sweater would be comfortable.")
    else:
        print("It's quite cold. You should wear a warm jacket or pullover to avoid getting cold.")

# Run the program
clothing_advisor()

