words = ["apple", "banana", "apple", "orange", "banana"]
# Create a new list to hold the modified words
modified_words = []

# Iterate through each word in the list
for word in words:
    # Check if the word is not already in the modified list
    if word not in modified_words:
        # If not, add it to the modified list
        modified_words.append(word)
        
# Print the modified list of words
print("Modified List of Words:")
for word in modified_words:
    print(word, end=' ')

# Print a new line for better readability
print()  # Print a new line for better readability