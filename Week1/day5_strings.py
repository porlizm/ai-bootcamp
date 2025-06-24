# String

first = "Hello"
second = "World"

result = first + " " + second
print(result)

text = "Python Programming"
print(text[0:6])
print(text[-5:])

name = "Porsche"
age = 33
print(f"My name is {name} and I am {age} years old.")

#split()
sentence = "Python is a powerful programming language."
words = sentence.split()
print("Words in the sentence:")
for word in words:
    print(word) 


# Join()
joined_sentence = " ".join(words)
print("\nJoined sentence:")
print(joined_sentence)

# Replace()
replaced_sentence = sentence.replace("powerful", "versatile")
print("\nReplaced sentence:")
print(replaced_sentence)

# Strip()
text_with_spaces = "   Hello, World!   "
stripped_text = text_with_spaces.strip()
print("\nStripped text:")
print(stripped_text)

# Find()
index = sentence.find("powerful")
if index != -1:
    print(f"\n'powerful' found at index: {index}") 
else:
    print("\n'powerful' not found in the sentence.")