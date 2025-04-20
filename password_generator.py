import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    # Ensure at least one of each selected type is included
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password
    password += random.choices(characters, k=length - len(password))
    random.shuffle(password)

    return ''.join(password)

def main():
    print("=== Secure Password Generator ===")

    # Ask for password length with validation
    while True:
        try:
            length_input = input("Enter password length: ")
            length = int(length_input)
            if length < 4:
                print("Password length should be at least 4 to include all character types.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Ask for character type preferences
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print("\nGenerated Password:", password)

        copy = input("Copy to clipboard? (y/n): ").lower()
        if copy == 'y':
            try:
                import pyperclip
                pyperclip.copy(password)
                print("Password copied to clipboard!")
            except ImportError:
                print("pyperclip module not found. Install it with 'python -m pip install pyperclip'")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
