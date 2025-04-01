import random
import string
def generate_password() :
    char = string.ascii_letters + string.digits # all letters and digits
    password = ""
    for i in range(8):
        password += random.choice(char) # adding a random charcter to password
    return password

print(f"Password: {generate_password()}")
