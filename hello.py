# My first Python program
# IS 303 - Build 1

# Interactive greeting program
name = input("What is your name? ")
print(f"Hello, {name}! Welcome to IS 303.")

# Tip Calculator
# Takes a meal total and calculates tips at different percentages

meal_total = float(input("What was your meal total? $"))

tip_15 = meal_total * 0.15
tip_18 = meal_total * 0.18
tip_20 = meal_total * 0.20

print(f"\nTip options for a ${meal_total:.2f} meal:")
print(f"  15% tip: ${tip_15:.2f}")
print(f"  18% tip: ${tip_18:.2f}")
print(f"  20% tip: ${tip_20:.2f}")
print(f"  Total with 18% tip: ${meal_total + tip_18:.2f}")

#Simply first_name/last_name output
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print("Hello, "+ first_name + " "+ last_name + ".")

#Fahrenheit to Celsius calculator
temp = int(input("What is the current temperature in Fahrenheit? "))
celsius = (temp - 32) * 5 / 9
print(f"{temp} F is {celsius:.1f} C")

#Weekly pay calculator
hours_worked = float(input("What was the total amount of hours worked? "))
hourly_pay = float(input("What is your hourly pay rate? $"))
print(f"  Your weekly pay is: ${hours_worked * hourly_pay:.2f}.")

# How much does a discount net me in savings?
price = float(input("Product price: $"))
discount_pct = float(input("Discount percentage: "))
discount_amount = price * (discount_pct / 100)
final_price = price - discount_amount

print(f"\nOriginal price: ${price:.2f}")
print(f"Discount ({discount_pct}%): -${discount_amount:.2f}")
print(f"Final price: ${final_price:.2f}")

