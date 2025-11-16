def calculate_product(numbers_tuple):
    product = 1
    for num in numbers_tuple:
        product *= num
    return product

# Example usage:
my_tuple = (2, 3, 4, 5)
result = calculate_product(my_tuple)
print(f"The product of the tuple elements is: {result}")