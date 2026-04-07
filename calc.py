def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error: Div by zero!"

print("--- Linux CLI Calculator ---")
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == '+': print(f"Result: {add(num1, num2)}")
elif op == '-': print(f"Result: {subtract(num1, num2)}")
elif op == '*': print(f"Result: {multiply(num1, num2)}")
elif op == '/': print(f"Result: {divide(num1, num2)}")
else: print("Invalid Operator")

