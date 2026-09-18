"""
# Q1

# Input student details
student_ID = input("Enter student ID: ")
first_name = input("Enter first name: ")
try:
    student_ID = int(student_ID)
except ValueError:
    print("INVALID STUDENT ID\nStudent ID must be in a 4 digits format")

# Input marks
math = int(input("Enter math marks(0-100): "))
programming = int(input("Enter programming marks(0-100): "))
physics = int(input("Enter physics marks(0-100): "))

# Calculate average
avg_mark = float((math + programming + physics) / 3)
print()

# Display formatted report card
print("====================================")
print("     STUDENT REPORT CARD     ")
print("====================================")
print("Student ID:", student_ID)
print("Name:", first_name)
print("-----------------------------")
print("Mathematics:", math)
print("Programming:", programming)
print("Physics:", physics)
print("-----------------------------")
print(f"Average Mark: {avg_mark:.1f}")
print("===================================")
"""

"""
# Q2 - Compound Interest Calculator

# Input values
p = float(input("Enter Principal amount: "))
r = float(input("Enter Annual interest rate (%): "))
t = int(input("Enter Time period (years): "))

# Calculations: final amount, total interest earned, % increase
a = p * ((1 + r / 100) ** t)
total_interest = a - p
percentage_increase = (total_interest / p) * 100

# Display results
print(f"Final Amount: {a:.2f}")
print(f"Total Interest Earned: {total_interest:.2f}")
print(f"Percentage Increase: {percentage_increase:.1f}%")
"""

"""
# Q3 - Unit Converter

# Input distance in kilometers
km = float(input("Enter distance in kilometers: "))

# Perform conversions
meters = km * 1,000
centimeters = km * 100,000
miles = km * 0.621371
feet = km * 3280.84

# Display conversion results
print("\n--- Distance Conversion Results ---")
print(f"Kilometers: {km}")
print(f"Meters: {meters:.1f}")
print(f"Centimeters: {centimeters:.1f}")
print(f"Miles: {miles:.2f}")
print(f"Feet: {feet:.1f}")
"""

# Q4 - Shipping Cost Calculator

weight = float(input("Enter package weight (kg): "))
zone = int(input("Enter destination zone (1-3): "))
fragile = input("Is the package fragile? (yes/no): ").lower()
fragile_fee = 0

import sys

# Inputs validation
if weight <= 0:
    print("Invalid weight. Must be greater than 0.")
    sys.exit()
elif zone not in [1, 2, 3]:
    print("Invalid zone. Must be 1, 2, or 3.")
    sys.exit()
elif fragile not in ["yes", "no"]:
    print("Invalid fragile input. Must be 'yes' or 'no'.")
    sys.exit()
else:
    # Base cost calc
    if zone == 1:
        base_cost = 5.00 + (2.50 * weight)
    elif zone == 2:
        base_cost = 8.00 + (3.50 * weight)
    else:
        base_cost = 12.00 + (5.00 * weight)

    total_cost = base_cost

    # calc fragile fee if applicable
    if fragile == "yes":
        fragile_fee = 3.50
        total_cost += fragile_fee

    # Calculate surcharge for obese packages
    if weight > 10:
        surcharge = total_cost * 0.15
        print(f"Heavy Package Surcharge (15%): ${surcharge:.2f}")
        total_cost += surcharge

    # Express delivery recommendation
    if zone == 3 or weight > 5:
        recommendation = "Yes"
    else:
        recommendation = "No"

# All outputs
print()
print(f"Base Cost: ${base_cost:.2f}")
if fragile_fee != 0:
    print(f"Fragile Handling: ${fragile_fee:.2f}")
print(f"Total Shipping Cost: ${total_cost:.2f}")
print(f"Express Delivery Recommended: {recommendation}")

