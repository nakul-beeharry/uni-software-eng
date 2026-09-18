#LEVEL 1 (EASY)

""" Q1 - Bill & Tip calculator

bill = float(input("Enter bill: $"))
percent_tip = int(input("Enter tip(%): "))
tip = bill * (percent_tip/100)
total = bill + tip
print(f"Amount of tip: ${tip}")
print(f"Total bill: ${total}")
"""
from _pyrepl.commands import end

""" Q2 - Username Formatter

full_name = input("Enter your full name: ")
print(len(full_name))
print(full_name.upper())
if full_name.startswith("A"):
    print(True)
else:
    print(False)
"""

#LEVEL 2 (MEDIUM)

""" Q3 - Character Classifier

user = input("Enter a string: ")
if user.endswith("ing"):
    print("Action word!")
elif user.startswith("un"):
    print("Reversed action!")
else:
    print("Regular word!")
"""

""" Q4 - Password Masker & Slicer

password = input("Enter a password(6 or more characters): ")
masked_pass = password[0] + "*" * (len(password)-2) + password[-1]
print(password)
"""

# LEVEL 3 (Basic for loops) - MID/HARD


""" Q5 - Multiples Counter

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
count = 0
for i in range(start, end + 1, 1):
    if i % 3 == 0:
        print(i)
        count +=1
print(f"Amount of multiples of 3 found: {count}")
"""

""" Q6 - Countdown Rocket Launch

start = int(input("Enter starting count: "))
for i in range(start, 0, -1):
    print(i)
print("BLAST OFF!")
"""

# LEVEL 4 - TRICKY/COMBINED LOGIC

""" Q7 - Countdown Rocket Launch

N = int(input("Enter a number: "))
sum_even = 0
for i in range(1, N + 1, 1):
    if i % 2 == 0:
        sum_even += i
print(sum_even)
"""

""" Q8 - Vowel Counter in String
"""

phrase = input("Enter a phrase: ")
vowel = ["a", "e", "i", "o", "u"]
vowel_count = 0
for char in phrase:
    for i in range(0 , len(vowel), 1):
        if char.lower() == vowel[i]:
            vowel_count += 1
print(vowel_count)