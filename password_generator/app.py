#!/usr/bin/python
"""password generator
"""
import random
import string

def generate() -> None:
    """
    Generates a random password of a specified length and prints it to the console.

    This function prompts the user to enter the desired length of the password and generates a random password
    using the `random.sample()` function. The password is a combination of uppercase and lowercase letters,
    digits, and punctuation characters. The generated password is then printed to the console.

    Parameters:
        None

    Returns:
        None

    Raises:
        ValueError: If the user enters an invalid input for the password length.

    Example:
        >>> generate()
        Generate Password
        Enter the length of the password: 10
        w3lk[=!2y
        Press q to quit or any other key to continue: q
    """
    print("Generate Password")
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            password = "".join(random.sample(string.ascii_letters + string.digits + string.punctuation, length))
            print(password)
            if input("Press q to quit or any other key to continue: ").lower() == "q":
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    generate()