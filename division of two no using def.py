def division(a, b):
    if b != 0:
        result = a / b
        print("Division =", result)
    else:
        print("Cannot divide by zero")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

division(x, y)