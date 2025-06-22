# function with parameters
def add_number(a, b):
    c = a + b
    return c

result = add_number(5, 3)
print("Sum: ", result)

# Local scope
def greet(name):
    greeting = f"Hello, {name}!"
    return greeting

greet("Porsche")
# print(greeting) error # because greeting is local to the function

# Global scope
greeting = "Hello, World!"

def say_hello():
    print(greeting + " from inside the function!")
    
say_hello()
print(greeting + " from outside the function!")  # This will work because greeting is in the global scope


# Module import example
import math
print("Square root of 16 is:", math.sqrt(16))  # Using the math module to calculate square root

# Importing specific function from a module
from math import sqrt
print("Square root of 25 is:", sqrt(25))  # Using the imported sqrt function from math module

# Use alias for a module
import math as m
print("Square root of 36 is:", m.sqrt(36))

# Creating a custom module
def porsche(name):
    """Prints a greeting message with the given name."""
    print(f"Hello, {name}! Welcome to Porsche Studio.")
    return f"Message sent to {name}."

porsche("Jelly")