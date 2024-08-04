import random
import string

def generate_password(length):
    # Define character sets for password generation
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the specified length
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    try:
        # Prompt the user to specify the desired length of the password
        length = int(input("Enter the desired length of the password: "))

        # Ensure the length is positive
        if length <= 0:
            print("Length should be a positive integer.")
            return
        
        # Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number for the length.")

if __name__ == "__main__":
    main()
