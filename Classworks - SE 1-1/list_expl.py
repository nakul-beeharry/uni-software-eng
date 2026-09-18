"""
1.
# Basics of lists
# can include multiple data types, has no extra space in memory
# len({list_name}) = number of elements in list
# append{list_name} = add new item at next available index in list

x = ["test", True, 10, 6.9]
print(x) #prints out all elements in list
print(x[2]) #prints out element at index 2 in list. for instance, x[2] = 10

x[2] = 15 #REPLACES current value at x[2] (10) by 15
print(x)
print(x[0])

print(len(x)) #prints length of list, that is NUMBER OF ELEMENTS

x.append("Hello") # .append({data}) to add new element in list at next available index
print(x)

x.pop(0) # .pop({index}) POPS/REMOVES item at specified index from list
print(x)

x.extend([15, 24, 39]) #unlike .append , .extend adds MULTIPLE ELEMENTS in the list
print(x)

if 24 in x: # checks if a value exists in the list
    print("Found")
else:
    print("Item Not Found")

"""
print()

#"""
2.
list(range(1,6,1))

y = list()
print(y)

y = []
numbers = [102, 569, 100, 9]
print(numbers[3])

numbers_length = len(numbers) #calculates and assign length of list/amt of values to variable

print(numbers[numbers_length-1]) #outputs element of list at last index way 1

print(numbers[len(numbers)-1]) #outputs element of list at last index way 2

print(numbers[-1]) #outputs element of list at last index way 3
print(numbers[-2]) #outputs element of list at one to last index

print()
# TRAVERSING A LIST USING A FOR LOOP
# Version 1
for i in numbers:
    print(i)

print()
# Version 2
for i in range(0 , len(numbers),1):
    print(numbers[i])

print()
# Version 2
for i in range(-4, 0,1):
    print(numbers[i])

#"""