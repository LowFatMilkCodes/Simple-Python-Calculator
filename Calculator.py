import math
import os

def clear_screen():
    # Clear screen for Windows, macOS, and Linux
    os.system("cls" if os.name == "nt" else "clear")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error: Cannot calculate square root of a negative number"

def logarithm(x, base):
    if x > 0 and base > 0 and base != 1:
        return math.log(x, base)
    else:
        return "Error: Invalid input for logarithm"

# Additional features

def factorial(x):
    if x >= 0:
        return math.factorial(x)
    else:
        return "Error: Cannot calculate factorial of a negative number"

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

# Main calculator loop

def calculator():
    while True:
        clear_screen()
        print("LowFatMilk Codes Calculator")
        print("-------------------")
        print("Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Square Root")
        print("7. Logarithm")
        print("8. Factorial")
        print("9. Sine")
        print("10. Cosine")
        print("11. Tangent")
        print("0. Exit")

        try:
            choice = int(input("Enter the operation number (0-11): "))

            if choice == 0:
                print("Exiting the calculator...")
                break

            if choice in [1, 2, 3, 4, 5]:
                clear_screen()
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == 1:
                    result = add(num1, num2)
                    print("Result: ", result)
                elif choice == 2:
                    result = subtract(num1, num2)
                    print("Result: ", result)
                elif choice == 3:
                    result = multiply(num1, num2)
                    print("Result: ", result)
                elif choice == 4:
                    result = divide(num1, num2)
                    print("Result: ", result)
                elif choice == 5:
                    result = power(num1, num2)
                    print("Result: ", result)

                input("Press enter to continue...")
                continue

            elif choice in [6, 7]:
                clear_screen()
                num = float(input("Enter the number: "))

                if choice == 6:
                    result = square_root(num)
                    print("Result: ", result)
                elif choice == 7:
                    base = float(input("Enter the base: "))
                    result = logarithm(num, base)
                    print("Result: ", result)

                input("Press enter to continue...")
                continue

            elif choice == 8:
                clear_screen()
                num = int(input("Enter the number: "))
                result = factorial(num)
                print("Result: ", result)

                input("Press enter to continue...")
                continue

            elif choice in [9, 10, 11]:
                clear_screen()
                angle = float(input("Enter the angle in degrees: "))

                if choice == 9:
                    result = sin(angle)
                    print("Result: ", result)
                elif choice == 10:
                    result = cos(angle)
                    print("Result: ", result)
                elif choice == 11:
                    result = tan(angle)
                    print("Result: ", result)

                input("Press enter to go back to menu")
                continue

            else:
                print("Invalid choice. Please enter a number between 0 and 11.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the calculator
calculator()
