import random
import string

print("================================")
print("   Secure Password Generator")
print("================================")

length = int(input("Enter password length: "))

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
numbers = string.digits
symbols = "@#$&*!"

all_characters = uppercase + lowercase + numbers + symbols

password = ""

password += random.choice(uppercase)
password += random.choice(lowercase)
password += random.choice(numbers)
password += random.choice(symbols)

for i in range(length - 4):
    password += random.choice(all_characters)

password_list = list(password)
random.shuffle(password_list)

final_password = "".join(password_list)

print("\nGenerated Secure Password:")
print(final_password)

print("\nSecurity Check")
print("✓ Contains Uppercase Letter")
print("✓ Contains Lowercase Letter")
print("✓ Contains Number")
print("✓ Contains Symbol")
