# Assume initial values
a = 10
b = 20
c = 30

# Print initial values
print(f"Initial values: a = {a}, b = {b}, c = {c}")

# Perform the circular swap
temp = a
a = b
b = c
c = temp

# Print swapped values
print(f"Swapped values: a = {a}, b = {b}, c = {c}")