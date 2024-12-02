# Functions

l = (40, 30, 50, 20)
print(l)

print("-----------------------------")

print("Maximum and minimum element in the list (For numbers it will be smaller or greater, and for alphabets it will start from A-Z")
maximum = max(l)
minimum = min(l)
print("Maximum value:", maximum, " Minimum value:", minimum)

print("-----------------------------")

print("Sum all the elements in the list (elements must be numbers)")
print(sum(l))

print("-----------------------------")

print("Sum all the elements in the list with an initializer (elements must be numbers)")
print(sum(l,20))

print("-----------------------------")

print("Getting the index position of an element : 50")
m=l.index(50,0)
print(m)

