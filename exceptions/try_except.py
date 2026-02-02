# Exception handling example

try:
    a = 10
    b = 0
    result = a / b
    print(result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

finally:
    print("Program execution completed")
