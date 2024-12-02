# Tuples are like lists. It is immutable
# We can't change/update any element in tuple

tupleVar = (5, 45, 8.9, 10, 5.5, 10)
print(type(tupleVar), tupleVar)

print("----------------------------------")

# Length of tuple

print("Length of tuple : ", len(tupleVar))

print("----------------------------------")

# Using loop to iterate a tuple

length = len(tupleVar)
print("Normal")
print()
for m in range(length):
    print(tupleVar[m])

print()
for p in tupleVar:
    print(p)

print("----------------------------------")

print("Reverse")
print()
for n in range(length-1,-1,-1):
    print(tupleVar[n])

print("----------------------------------")