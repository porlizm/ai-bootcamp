# Example 1: Checking a condition
num = 10
if num > 5:
    print("Number is greater than 5")
elif num == 5:
    print("Number is equal to 5")
else:
    print("Number is less than 5")

# Example 2: Nested if statements
age = -20
if age >= 18:
    print("You are an adult")
    if age >= 65:
        print("You are a senior citizen")
else :
    print("You are a kid")


# Example 3: Using a list in a condition
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        print("Found a banana!")
    else:
        print(fruit)
        
# Example 4: Loops with range
for i in range(5):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
        
# Example 5: Using a while loop
count = 5
while count > 0:
    print(f"Count is {count}")
    count -= 1
    
# Example 6: Using a break statement
for i in range(10):
    if i == 5:
        print("Breaking the loop at 5")
        break
    print(i)

# Example 7: Using a continue statement
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"{i} is odd, continuing to next iteration")


