decimal_number = int(input("Enter a number: "))
binary_number = ""

if decimal_number == 0:
    binary_number = "0"
else:
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = int(remainder) + binary_number
        decimal_number = decimal_number // 2

print("The binary equivalent is:", binary_number)