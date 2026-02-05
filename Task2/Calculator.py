# Interactive Calculator Project

def addition(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def show_menu():
    print("\n====== CALCULATOR MENU ======")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. View Calculation History")
    print("6. Exit")


history = []

while True:
    show_menu()
    choice = input("Enter the number of your choice (1-6): ")

    if choice == "6":
        print("Thank you for using calculator!")
        break

    if choice == "5":
        if not history:
            print("No calculations done.")
        else:
            print("\n--- Calculation History ---")
            for item in history:
                print(item)
        continue

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue

    if choice == "1":
        result = addition(num1, num2)
        operation = "+"
    elif choice == "2":
        result = subtract(num1, num2)
        operation = "-"
    elif choice == "3":
        result = multiply(num1, num2)
        operation = "*"
    elif choice == "4":
        result = divide(num1, num2)
        operation = "/"

    print(f"Result: {num1} {operation} {num2} = {result}")
    history.append(f"{num1} {operation} {num2} = {result}")
