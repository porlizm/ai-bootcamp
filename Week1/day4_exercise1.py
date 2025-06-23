person = {"name": "John", "age": 30, "grade": "A"}

# Add new key-value pair
person["city"] = "Austin"

person["age"] = 33

if "grade" in person:
    del person["grade"]
    

# Print the updated dictionary
print(person)
