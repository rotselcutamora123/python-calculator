def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def calculator():
    print("Simple Calculator")
    
    # Input Data
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    
    # Check Operation
    if operation == '+':
        result = add_numbers(num1, num2)
    elif operation == '-':
        result = subtract_numbers(num1, num2)
    elif operation == '*':
        result = multiply_numbers(num1, num2)
    elif operation == '/':
        result = divide_numbers(num1, num2)
    else:
        result = "Invalid operation"
    
    # Show Result
    print(f"Result: {result}")

# Run the calculator
calculator()