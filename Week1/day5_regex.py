import re

text = "Contact us at 012-345-6789 or 987-654-3210"
digits = re.findall(r'\d+', text)

print("Digits found:", digits)

update_text = re.sub(r"\d+", "X", text)
print("Updated text:", update_text)

