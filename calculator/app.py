#!/usr/bin/python

"""simple calculator app
"""

def calculator() -> None:
    """
    A simple calculator function that takes user input for two numbers and an operator to perform basic arithmetic operations.
    Handles exceptions for invalid input, invalid operators, and zero division errors.
    """

    operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
    }

    print("Simple Calculator")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            result = operations[operator](num1, num2)
            print("Result:", num1 , operator, num2, "=", result)
            # q to quit the program or any other key to continue
            if input("Press q to quit or any other key to continue: ").lower() == "q":
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except KeyError:
            print("Invalid operator. Please enter a valid operator.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")

if __name__ == '__main__':
    calculator()