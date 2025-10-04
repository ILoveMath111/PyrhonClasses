# Function to calculate powers
def calculate_powers(base, exponents):
    powers = []
    for exp in exponents:
        powers.append(base ** exp)
    return powers

# Main program
def main():
    print("Power Calculator by Vrisha")
    
    base = float(input("Enter the base number: "))
    
    n = int(input("Enter how many powers you want to calculate: "))
    exponents = []
    
    for i in range(n):
        exp = int(input(f"Enter exponent {i+1}: "))
        exponents.append(exp)
    
    results = calculate_powers(base, exponents)
    
    print("\nResults:")
    for i in range(n):
        print(f"{base}^{exponents[i]} = {results[i]}")

# Run the program
if __name__ == "__main__":
    main()
