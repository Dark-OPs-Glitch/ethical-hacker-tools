import random
import string

print("=== HACKER PASSWORD GENERATOR ===")
length = int(input("How long do you want the password? "))

chars = string.ascii_letters + string.digits + "!@#$%^&*"
password = ''.join(random.choice(chars) for _ in range(length))

print("\nYour strong password:", password)