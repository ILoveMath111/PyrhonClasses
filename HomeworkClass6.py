char = input("Enter a character: ")

if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
    print(f"The character '{char}' is an alphabet.")
else:
    print(f"The character '{char}' is not an alphabet.")