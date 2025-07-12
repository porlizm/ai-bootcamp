#Write a program to copy the contents of one file to another

def copy_file_contents(source_file, destination_file):
    try:
        with open(source_file, "r") as src:
            content = src.read()
            
        with open(destination_file, "w") as dest:
            dest.write(content)
        print(f"Contents copied from {source_file} to {destination_file} successfully.")
    
    except FileNotFoundError:
        print(f"Error: The file '{source_file}' does not exist.")
    
    except Exception as e:
        print(f"Error copying file contents: {e}")

# Example usage
copy_file_contents("fruits.txt", "copy_fruits.txt")