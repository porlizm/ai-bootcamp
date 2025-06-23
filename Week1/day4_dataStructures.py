num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

fruits = ["apple", "banana", "cherry",]

mixed_list = [1, "apple", 3.14, True]

print(num[2])
print(fruits[0])
print(mixed_list[1])

fruits.append("orange")
print(fruits)

fruits.insert(1, "kiwi")
fruits.remove("banana")
print(fruits)

del fruits[0]  # Deletes the item at index 1
print(fruits)

fruits.pop()  # Removes the last item
print(fruits)

sliced_fruits = fruits[1:3]  # Slicing the list from index 1 to 2
print(sliced_fruits)

colors = ("red", "green", "blue")
single_item = ("yellow",)  # Tuple with a single item must have a comma

print(colors[0])  # Accessing tuple elements
print(colors[-2])


#Dictionaries
student = {
    "name": "John",
    "age": 20,
    "courses": ["Math", "Science", "History"],
    "grade": "A",
}
print(student["name"])  # Accessing dictionary values
print(student.get("age"))  # Using get method to access value
print(student.get("address", "Not Found"))  # Default value if key not found

# Adding a new key-value pair
student["address"] = "123 Main St"
print(student)

# Updating an existing key-value pair
student["grade"] = "A+"
print(student)

# Removing a key-value pair
del student["age"]
print(student)

# Iterating through dictionary keys and values
for key, value in student.items():
    print(f"{key}: {value}")
    
# Checking if a key exists in the dictionary
if "name" in student:
    print("Name exists in the student dictionary.")
    
# Sets
fruits_set = {"apple", "banana", "cherry"}
print(fruits_set)  # Printing the set

# Adding an item to the set
fruits_set.add("orange")
print(fruits_set)

# Removing an item from the set
fruits_set.remove("banana")
print(fruits_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}  


# Union of two sets
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)
print(set1 | set2)  # Alternative way to get union using the '|' operator

# Intersection of two sets
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)
print(set1 & set2)

# Difference of two sets
difference_set = set1.difference(set2)
print("Difference of set1 and set2:", difference_set)
print(set1 - set2)  # Alternative way to get difference using the '-' operator

# Symmetric difference of two sets
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference of set1 and set2:", symmetric_difference_set)
print(set1 ^ set2)  # Alternative way to get symmetric difference using the '^' operator

# Checking if a set is a subset of another
is_subset = set1.issubset(set2)
print("Is set1 a subset of set2?", is_subset)


