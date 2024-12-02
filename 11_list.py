# List is like array. It is mutable
# We can change/update any element in list

arrList = [1, 'Python', 1.3, True, "Hello", 5, 7.9,False]
print(type(arrList), arrList)

print("----------------------------------")

# Length of list

print("Length of list : ", len(arrList))

print("----------------------------------")

# Index of a list

print("Getting index value")
print()
# Index no . -> [0,1,2,....(length-1)] or [length, length-1, length-2,..., 1]

print(arrList[1]) # getting index no. 1 from left
print(arrList[-2]) # getting index no. 2 from right

print("----------------------------------")

#  Slicing a string (including space)

# arrList[Start index: Ending index: Increment/Decrement]
print("Slicing a list")
print()
print(arrList[0:2]) # Starting from 0 from left and ending at 2nd indexed position
print(arrList[0::2]) # Starting from 0 from left and ending at last indexed position with an increment of 2
print(arrList[0:7:1]) # Starting from 0 from left and ending at 6th indexed position with an increment of 1
print(arrList[-1::-1]) # Starting from 1 from right and ending at start position with a decrement of 1

print("----------------------------------")

# Using loop to iterate a list

length = len(arrList)
print("Normal")
print()
for m in range(length):
    print(arrList[m])

print()
for p in arrList:
    print(p)

print("----------------------------------")

print("Reverse")
print()
for n in range(length-1,-1,-1):
    print(arrList[n])

print("----------------------------------")

# List Comprehension

print("List Comprehension (Long method)")
l = []
for a in range(1,101):
    l.append(a)
print(l)
print()

print("List Comprehension (Short method)")
m = [n for n in range(1,101)]
print(m)
print()

print("List Comprehension with condition")
m = [n for n in range(1,101) if n%2==0]
print(m)