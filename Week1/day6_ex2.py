#Write and read a list of Items

def write_items_to_file(filename, items):
    try:
        with open(filename, "w") as file:
            for item in items:
                file.write(f"{item}\n")
                
        print(f"Items written to {filename} successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")
        
        
def read_items_from_file(filename):
    try:
        with open(filename, "r") as file:
            items = file.readlines()
            print("Items in the file:")
            for item in items:
                print(item.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        
# Example usage
fruits = ["Apple", "Banana", "Cherry", "Date"]
write_items_to_file("fruits.txt", fruits)
read_items_from_file("fruits.txt")