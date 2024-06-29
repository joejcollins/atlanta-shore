"""Starting point for console access to the package."""
# console_app_with_help.py

import argparse


def add_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}")


def subtract_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print(f"The difference between {num1} and {num2} is {result}")


def multiply_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print(f"The product of {num1} and {num2} is {result}")


def main():
    # Create the parser
    parser = argparse.ArgumentParser(
        description="Simple Arithmetic Console Application"
    )

    # Add an argument for the operation
    parser.add_argument(
        "operation",
        type=str,
        choices=["add", "subtract", "multiply"],
        help="The operation to perform",
    )

    # Parse the arguments
    args = parser.parse_args()

    # Perform the selected operation
    if args.operation == "add":
        add_numbers()
    elif args.operation == "subtract":
        subtract_numbers()
    elif args.operation == "multiply":
        multiply_numbers()


if __name__ == "__main__":
    main()
