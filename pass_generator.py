import random
import string

def generate_password(length=12, use_special_chars=True, use_digits=True, use_uppercase=True, use_lowercase=True):
    # Creating a pool of characters based on user preferences
    char_pool = ""
    
    if use_uppercase:
        char_pool += string.ascii_uppercase  # A-Z
    if use_lowercase:
        char_pool += string.ascii_lowercase  # a-z
    if use_digits:
        char_pool += string.digits  # 0-9
    if use_special_chars:
        char_pool += string.punctuation  # Special characters like !, @, #

    # Ensure the pool is not empty
    if not char_pool:
        raise ValueError("At least one character type should be selected.")

    # Generate a random password using the pool of characters
    password = ''.join(random.choice(char_pool) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    
    # Taking user input for password requirements
    length = int(input("Enter the desired length of the password: "))
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'

    # Generate password
    password = generate_password(length, use_special_chars, use_digits, use_uppercase, use_lowercase)
    
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
