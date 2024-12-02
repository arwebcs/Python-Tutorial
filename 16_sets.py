# Sets are unique elements of a list
# Set has no order

sets={10, 20, 30, 10}
print(type(sets), sets)
print()

# Iteration of a set
for n in sets:
    print(n)

print("------------------------------------------")

print("Transform a list into set")

l = [100, 200, 300, 100]
print(l)
s=set(l)
print(s)
print()
print("Add an element into set")
s.add(400)
print(s)
print()
print("Add a list of elements into set")
s.update([60,50,10])
print(s)
print("Pop first element from set")
print(s.pop())
print(s)
print()
print("Remove an element from set")
s.remove(400)
print(s)
print()
print("Discard/Remove an element from set")
s.discard(10)
print(s)
print()
print("Clear set")
s.clear()
print(s)