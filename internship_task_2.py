def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Modulus by zero not allowed"
    return a % b

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

print(f"Addition = {add(n1, n2)}")
print(f"Subtraction = {subtract(n1, n2)}")
print(f"Multiplication = {multiply(n1, n2)}")
print(f"Division = {divide(n1, n2)}")
print(f"Modulus = {modulus(n1, n2)}")
