#Create a Text Cleaner using Regular Expressions
import re

def clean_text(text):
    # Remove special characters except for spaces
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    
    # Remove extra spaces
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    return cleaned_text

# Example usage
input_text = "Hello, World!   This is a test.  Let's clean this text."
cleaned_text = clean_text(input_text)
print("Original Text:", input_text)
print("Cleaned Text:", cleaned_text)