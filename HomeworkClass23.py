# The given test dictionary (example)
test_dict = {'ide': 3, 'Gfg': 3, 'code': 2, 'course': 3, 'site': 2}

# Dictionary to store the frequency of values
frequency_dict = {}

# Iterate over all values in the test dictionary
for value in test_dict.values():
    # Use the get() method to check if the value is already a key in the frequency dictionary
    # If it is, increment its count; otherwise, set its count to 1
    frequency_dict[value] = frequency_dict.get(value, 0) + 1

# Print the resulting frequency dictionary
print("The frequency dictionary:", frequency_dict)
