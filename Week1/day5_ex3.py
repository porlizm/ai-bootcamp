#Write a program to count the number of vowels in a given string.

def count_vowels(text):
    # Define a set of vowels
    vowels = set("aeiouAEIOU")
    
    # Count the number of vowels in the text
    count = sum(1 for char in text if char in vowels)
    
    return count

# Example usage
input_text = input("Enter a string to count the vowels: ")
vowel_count = count_vowels(input_text)
print(f"The number of vowels in the input text is: {vowel_count}")

