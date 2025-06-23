sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Initiialize Dictionary to hold the count of each word
word_count = {}

# Count words fequency
for word in words:
    # Convert word to lowercase to ensure case insensitivity
    word_lower = word.lower()
    if word_lower in word_count:
        word_count[word_lower] += 1
    else:
        word_count[word_lower] = 1
        
# Print the word count dictionary
print("Word Count Dictionary:")
for word, count in word_count.items():
    print(f"{word}: {count}")