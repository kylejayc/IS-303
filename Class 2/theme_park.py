'''

Inputs:
- age
- day of the week
- height
- VIP
- waiver signed
- parent present

Processes: 
- Use the processes to identify wich rides are available

Outputs: 
- A list of rides

'''

# System prompts all user inputs
age = int(input("Age: "))
day_of_week = input("Day of week: ").lower()
height = int(input("Height in inches: "))
vip = input("VIP pass? Yes/No: ").upper()
waiver_signed = input("Waiver signed? Yes/No: ").upper()
parent_present = input("Is a parent present? Yes/No: ").upper()

# Mega Drop ride
if age >= 14 and waiver_signed == "yes" and (height >= 54 or (vip == "yes" and height >= 50)):
    print("You can ride the Mega Drop.")

if age >=14 and waiver_signed == "yes":
    if height >= 54:
        print("You can ride the Mega Drop.")
    elif vip == "yes" and height >= 50:
        print("You can ride the Mega Drop.")

# Thunderbolt ride
if age >= 10 and height >= 48 and day_of_week != "monday":
    print("You can ride the Thunderbolt.")

# Kiddie ride
if age > 8 or parent_present == "yes":
    print("You can ride the kiddie ride.")
    ride_found = True
else:
    print("No ride found.")

if ride_found == False:
    print("No ride found.") 