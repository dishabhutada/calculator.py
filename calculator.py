print("Hello! Welcome to the basic calculator!")
print("List of operations available:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")


a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
operation = input("Enter the operation you want to perform (+, -, *, /): ")


if operation == '+':
    print("Addition:", a + b)

elif operation == '-':
    print("Subtraction:", a - b)

elif operation == '*':
    print("Multiplication:", a * b)

elif operation == '/':
    if b == 0:
        print("Error: Cannot divide by zero.")
    else:
        print("Division:", a / b)

else:
    print("Invalid operation. Please enter one of: +, -, *, /")
