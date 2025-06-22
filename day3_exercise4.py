# Create module for string operations, including functions to reverse a string, count vowels, and check if a string is a palindrome.

# string_operations.py
def reverse_string(s):
    """Reverses the given string."""
    return s[::-1]

def count_vowels(s):
    """Counts the number of vowels in the given string."""
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

def is_palindrome(s):
    """Checks if the given string is a palindrome."""
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_s == cleaned_s[::-1]


print(reverse_string("hello"))
print(count_vowels("hello"))

print(is_palindrome("level"))  # Should return True
print(is_palindrome("hello"))  # Should return False