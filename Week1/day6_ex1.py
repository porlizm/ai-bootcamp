def count_words_and_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            lines_count = len(lines)
            words_count = sum(len(line.split()) for line in lines)
            
            print(f"Number of lines: {lines_count}")
            print(f"Number of words: {words_count}")
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        

count_words_and_lines("sample.txt")