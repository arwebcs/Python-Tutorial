# Functions

l = [40, 30, 50, 20]
print(l)

print("-----------------------------")

print("Insert an element at the specified index")
l.insert(0, 10)
print(l)

print("-----------------------------")

print("Append an element at last position")
l.append(70)
print(l)

print("-----------------------------")

print("Extend a list at the last position")
l.extend([100, 110])
print(l)

print("-----------------------------")

print("Update an element at the specified index")
l[6]=80
print(l)

print("-----------------------------")

print("Count an  element in the list. For ex. 30 ")
t = l.count(30)
print(t)

print("-----------------------------")

print("Get the index value of an element in the list. For ex. 30")

print(l.index(30))

print("-----------------------------")

print("Maximum and minimum element in the list (For numbers it will be smaller or greater, and for alphabets it will start from A-Z")
maximum = max(l)
minimum = min(l)
print("Maximum value:", maximum, " Minimum value:", minimum)

print("-----------------------------")

print("Sort the list (Always in ascending order)")
l.sort()
print(l)

print("-----------------------------")

print("Reverse the list (Always in descending order)")
l.reverse()
print(l)

print("-----------------------------")

print("Sum all the elements in the list (elements must be numbers)")
print(sum(l))

print("-----------------------------")

print("Delete the element of the specific index")
del l[1]
print(l)

print("-----------------------------")

print("Pop the element of the specific index. It will return the popped value")
print(l.pop(1))
print(l)

print("-----------------------------")

print("Remove an element of the list")
l.remove(20)
print(l)

print("-----------------------------")

print("Clear the list")
l.clear()
print(l)