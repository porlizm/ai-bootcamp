import re

# palindrome checker
def is_palindrome(text):
    text = "".join(char.lower() for char in text if char.isalnum())
    # Check if the cleaned text is equal to its reverse
    return text == text[::-1]

input_text = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(input_text):
    print(f'"{input_text}" is a palindrome.')
else:
    print(f'"{input_text}" is not a palindrome.')
    
