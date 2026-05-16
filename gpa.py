# Student records
students = [
    {"name": "Alice", "gpa": 3.8},
    {"name": "Bob", "gpa": 2.9},
    {"name": "Carol", "gpa": 3.5},
    {"name": "David", "gpa": 3.2},
    {"name": "Eve", "gpa": 3.9}
]

# TODO: Calculate the average GPA (accumulator)

# TODO: Find the student with the highest GPA (min/max)

# TODO: Find all students with GPA above 3.5 (filter)

# Hint: you can do all three in one loop!

total_gpa = 0              # Accumulator
highest_gpa = 0            # For max
top_student = None         # Track the name
high_achievers = []        # Filter list

for student in students:
    gpa = student["gpa"]
    name = student["name"]
    # Task 1: Accumulator - sum all GPAs
    total_gpa += gpa
    # Task 2: Find max - track highest GPA
    if gpa > highest_gpa:
        highest_gpa = gpa
        top_student = name
    # Task 3: Filter - collect students with GPA > 3.5
    if gpa > 3.5:
        high_achievers.append(name)

average_gpa = total_gpa / len(students)

print(f"Average GPA: {average_gpa:.2f}")
print(f"Highest GPA: {top_student} ({highest_gpa})")
print(f"High achievers (GPA > 3.5): {high_achievers}")