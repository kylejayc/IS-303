'''

Inputs:
- name
- height
- weight
- age
- sex

Processes:
- Input validation 
- Calculate BMI - weight / height^2 * 703
- Categorize BMI 
	- underweight < 18.5
	- healthy 18.5 - 24.9
	- overweight 25.0 - 29.9
	- obesity 30.0 - 39.9
	- severe obesity 40+

Outputs:
- Report for an individual

'''

#Collect user input
name = input("Name: ")
age = input("Age: ")
sex = input("Sex: ")
height = input("Height (inches): ")
weight = input("Weight (pounds): ")

#Input validation
age = age.replace(".","",1)
age_integer = age.isdigit()
if age_integer == True:
	age = int(age)
age_reasonable = False
if age_integer == True and age > 1 and age < 140:
	age_reasonable = True

sex = sex.lower()
sex_valid = False
if sex == "male" or sex == "female":
	sex_valid = True

height = height.replace(".","",1)
height_integer = height.isdigit()
if height_integer == True:
	height = int(height)
height_reasonable = False
if height_integer == True and height >= 12 and height <= 140:
	height_reasonable = True

weight = weight.replace(".","",1)
weight_integer = weight.isdigit()
if weight_integer == True:
	weight = int(weight)
weight_reasonable = False
if weight_integer == True and weight >= 1 and weight <= 1200:
	weight_reasonable = True

ready_to_process = True

if age_integer == False or age_reasonable == False:
	print("You entered a non-expected age. Please use whole numbers.")
	ready_to_process = False

if sex_valid == False:
	print("You entered an invalid sex. Please enter male or female.")
	ready_to_process = False

if height_integer == False or height_reasonable == False:
	print("You entered an unexpected height in inches. Please use whole numbers between 12 and 140.")
	ready_to_process = False

if weight_integer == False or weight_reasonable == False:
	print("You entered an unexpected weight in pounds. Please use whole numbers between 1 and 1200.")
	ready_to_process = False

# Print BMI output and report
if ready_to_process == True:
	bmi = (weight / height ** 2) * 703
	bmi_category = ""
	if bmi < 18.5:
		bmi_category = "underweight"
	elif bmi <= 24.9:
		bmi_category = "healthy"
	elif bmi <= 29.9:
		bmi_category = "overweight"
	elif bmi <= 39.9:
		bmi_category = "obese"
	else:
		bmi_category = "severe obesity"
# Report
print(f"Report for {name}\n"
        f"{age} year old {sex}\n"
        f"Your BMI is {bmi}\n"
        f"Your BMI category is: {bmi_category}")