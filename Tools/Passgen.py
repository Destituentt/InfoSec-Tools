import string
import random

# Function to generate random password of length
def passgen(length: int = 15):
    # Set of characters to choose from
    chars = string.ascii_letters + string.digits + string.punctuation
    # Generate random password
    password = "".join(random.choice(chars) for i in range(length))
    # Return password
    return password

password = passgen()
print(f'Your password is: {password}')
