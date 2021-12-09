import string
import random
char = list(string.ascii_letters + string.digits + "!@#$%^&*()")
def generate_random_password():
    len = int(input("Enter password length: "))
    random.shuffle(char)
    password = []
    for i in range(len):
        password.append(random.choice(char))
    random.shuffle(password)
    print("".join(password))

generate_random_password()