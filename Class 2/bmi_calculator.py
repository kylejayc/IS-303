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
age_reasonable = True
if age > 140 or age < 1:
    age_reasonable = False

sex = sex.lower()
sex_valid = False
if sex == "male" or sex == "female":
    sex_valid = True

height = height.replace(".","",1)
height_integer = height.isdigit()
height_reasonable = True
if height < 12 or height > 140:
    height_reasonable = False

weight = weight.replace(".","",1)
weight_integer = weight.isdigit()
weight_reasonable = True
if weight < 1 or weight > 1200:
    weight_reasonable = False

               

               