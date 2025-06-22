# fuction of check if a number is even or odd
def is_even_or_odd(number):
    """Check if a number is even or odd."""
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

number = int(input("Enter number to check even or odd: ",))

is_even_or_odd_result = is_even_or_odd(number)
print("The number: ", is_even_or_odd_result)