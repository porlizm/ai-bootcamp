# stores student names, scores, and ages in dictionary format and calculates the average grade.

# Initialize a dictionary to hold student data
students = {
    "Alice": {"score": 85, "age": 20},
    "Bob": {"score": 90, "age": 22},
    "Charlie": {"score": 78, "age": 21},
    "David": {"score": 92, "age": 23}
}

# Initialize variables to hold total score and count of students
total_score = 0
count = 0

# Iterate through the dictionary to calculate total score and count
for student, data in students.items():
    total_score += data["score"]
    count += 1
    
# Calculate the average score
average_score = total_score / count if count > 0 else 0

# Print the average score
print(f"Average Score: {average_score:.2f}")
