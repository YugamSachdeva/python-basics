# Simple calculator using match-case

num1 = 10
num2 = 5
choice = 1

match choice:
    case 1:
        print(num1 + num2)
    case 2:
        print(num1 - num2)
    case 3:
        print(num1 * num2)
    case 4:
        print(num1 / num2 if num2 != 0 else "Cannot divide by zero")
    case _:
        print("Invalid choice")
