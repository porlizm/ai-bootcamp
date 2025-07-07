#Create a program to find and replace all email addresses in a text using regular expressions.

import re

def replace_email_addresses(text, replacement="REDACTED"):
    # Regular expression pattern to match email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Replace all occurrences of the email addresses with the replacement text
    updated_text = re.sub(email_pattern, replacement, text)
    
    return updated_text

# Example usage
input_text = "Please contact us at support@example.com for assistance."
output_text = replace_email_addresses(input_text)
print(output_text)

# This will output: "Please contact us at REDACTED for assistance."