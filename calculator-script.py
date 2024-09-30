def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    while True:
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            operation = input("Choose operation (+, -, *, /): ")

            if operation == '+':
                result = add(x, y)
            elif operation == '-':
                result = subtract(x, y)
            elif operation == '*':
                result = multiply(x, y)
            elif operation == '/':
                result = divide(x, y)
            else:
                print("Invalid operation. Please try again.")
                continue

            print(f"Result: {result}")

            again = input("Do you want to perform another calculation? (y/n): ")
            if again.lower() != 'y':
                break

        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    print("Thank you for using the calculator!")

if __name__ == "__main__":
    calculator()
