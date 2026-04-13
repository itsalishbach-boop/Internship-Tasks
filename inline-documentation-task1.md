# Define a function to add two numbers
def add(x, y): 
    return x + y  # Returns the sum of x and y

# Define a function to subtract one number from another
def subtract(x, y): 
    return x - y  # Returns the difference between x and y

# Define a function to multiply two numbers
def multiply(x, y): 
    return x * y  # Returns the product of x and y

# Define a function to divide two numbers, with zero division handling
def divide(x, y): 
    return x / y if y != 0 else "Error: Div by zero!"  # Prevent division by zero

# Display calculator header
print("--- Linux CLI Calculator ---")

# Take the first number as input and convert it to a float
num1 = float(input("Enter first number: "))

# Take the operator as input (+, -, *, /)
op = input("Enter operator (+, -, *, /): ")

# Take the second number as input and convert it to a float
num2 = float(input("Enter second number: "))

# Perform the operation based on the operator entered
if op == '+': 
    print(f"Result: {add(num1, num2)}")  # Call add() if '+' is entered
elif op == '-': 
    print(f"Result: {subtract(num1, num2)}")  # Call subtract() if '-' is entered
elif op == '*': 
    print(f"Result: {multiply(num1, num2)}")  # Call multiply() if '*' is entered
elif op == '/': 
    print(f"Result: {divide(num1, num2)}")  # Call divide() if '/' is entered
else: 
    print("Invalid Operator")  # Handle invalid operator input

