import random
import string

def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_lowercase
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


print("==== PASSWORD GENERATOR APPLICATION ====")
print("Select Password Complexity")
print("1. Low  (Lowercase letters)")
print("2. Medium (Letters + Numbers)")
print("3. High (Letters + Numbers + Symbols)")

try:
    length = int(input("Enter the password length: "))
    if length < 6:
        print("Password length should be at least 6 characters.")
        exit()

    complexity = int(input("Enter complexity choice (1/2/3): "))

    password = generate_password(length, complexity)

    if password:
        print("\nGenerated Password:", password)
    else:
        print("Invalid complexity choice.")

except ValueError:
    print("Invalid input. Please enter numeric values only.")

