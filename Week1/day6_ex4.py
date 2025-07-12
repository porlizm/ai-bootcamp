#Create a program that counts the number of occurrences of a specific word in a file

def count_word_occurrences(filename, word):
    try:
        with open(filename, "r") as file:
            content = file.read()
            word_count = content.lower().count(word.lower())
            print(f"The word '{word}' occurs {word_count} times in the file.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Example usage
count_word_occurrences("fruits.txt", "Jelly")