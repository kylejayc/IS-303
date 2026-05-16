food = ""

if food:
    print("True")
else:
    print("False")


name = "Kyle"
food = ""

if food and name:
    form_complete = True

if form_complete:
    print(f"{name}'s favorite food is {food}")
else:
    print("Please fill out the form completely.")


age = input("Age: ")
if int(age) < 0:
    print("Invalid age")
elif int(age) < 18:
    print("Minor")
else:
    print("Adult")