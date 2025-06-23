# Reverse a list and remove duplicates using a set

words = ["apple", "banana", "apple", "orange", "banana"]

# Create a new list to hold the modified words
modified_words = []

# Create a set to track seen words
seen_words = set()

# Iterate through each word in the list
for word in reversed(words):
    # Check if the word is not already in the seen set
    if word not in seen_words:
        # If not, add it to the modified list and the seen set
        modified_words.append(word)
        seen_words.add(word)
        
# Print the modified list of words
print("Modified List of Words:")
for word in modified_words:
    print(word, end=' ')

# Print a new line for better readability
print()  # Print a new line for better readability

