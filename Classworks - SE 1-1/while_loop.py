
#1 simple while loop to output numbers 1 to 5
x = 1
while(x<6):
    print(x)
    x += 1

print()
#2 while loop to take an input and keep running until user inputs "n or N"
x = "y"
while(x!= "n"):
    print("udm")
    ans = input("Do you wish to continue? (y/n): ")
    x = ans.lower()

print()
#3 while loop with a break statement
while(True):
    print("UDM")
    ans = input("Do you wish to continue? (y/n): ")
    if ans.lower() == "n":
        break
    else:
        continue


print()
#4 for loop and while loop performing the same thing (for loop -> while loop)
# for loop version
for x in range(1,6,1):
    for y in range(1, x+1, 1):
        print(y)
    print("\n")


print()
# while loop version
x = 1
while(x<6):
    y = 1
    while(y < x + 1):
        print(y)
        y += 1
    print("\n")
    x += 1
