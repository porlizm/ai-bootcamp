#Write a program to reverse a string using regular expressions.
import re

def reverse_string(text):
    # Use regular expression to find all characters in the string
    characters = re.findall(r'.', text)
    
    # Reverse the list of characters
    reversed_characters = characters[::-1]
    
    # Join the reversed characters back into a string
    reversed_text = ''.join(reversed_characters)
    
    return reversed_text

# Example usage
input_text = input("Enter a string to reverse: ")
reversed_text = reverse_string(input_text)
print("Reversed Text:", reversed_text)

