def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b 

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns the quotient of a and b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

while True:
    print("\n##################################################")
    print("Exercise 2: Simple Calculator")
    print("##################################################")
    
    print("\nMenu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
    
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please try again.")
        continue
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == '1':
            result = add(num1, num2)
            print(f"The result of {num1} + {num2} is: {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"The result of {num1} - {num2} is: {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"The result of {num1} * {num2} is: {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"The result of {num1} / {num2} is: {result}")
    except ValueError as e:
        print(f"Error: {e}. Please enter valid numbers.")
    