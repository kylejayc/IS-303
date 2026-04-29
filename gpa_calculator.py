# Kyle Christensen
#IS 303 | Giboney

'''Inputs
- Student name
- Grade for three classes
- Credits for three classes'''

name = input("Student name: ")

grade_1 = int(input("Course 1 grade point: "))
grade_2 = int(input("Course 2 grade point: "))
grade_3 = int(input("Course 3 grade point: "))

credit_1 = int(input("Course 1 credit amount: "))
credit_2 = int(input("Course 2 credit amount: "))
credit_3 = int(input("Course 3 credit amount: "))


#Processes
# - Calculate GPA using grades and credit total

total_credits = credit_1 + credit_2 + credit_3
gpa = (grade_1 * credit_1 + grade_2 * credit_2 + grade_3 * credit_3) / (total_credits)


#Outputs
# - GPA and report card for student

print(f"{name}'s Report Card")
print(f"Credits taken: {total_credits}")
print(f"Course 1: {grade_1} credits: {credit_1} \n"
    f"Course 2: {grade_2} credits: {credit_2} \n"
    f"Course 3: {grade_3} credits: {credit_3}")