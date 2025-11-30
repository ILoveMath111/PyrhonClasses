import random
import string

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
length = 12  # Example length

password_list = [random.choice(characters) for i in range(length)]
random.shuffle(password_list)
password = "".join(password_list)

print(f"Generated Password: {password}")