a = 'Hello Python'
b = "Good Course"
print(a)
print(b)

print("----------------------------------")

# To join (concatenate) the two strings
print("Concatenation/joining of two strings (By + sign): " + a + "" + b)
print("Concatenation/joining of two strings (By , sign): ", a, "", b)

# N.B.: '+' sign will validate same data type. If not string, it will give error

print("----------------------------------")

# Length of string

print("Length of string '" + a + "' : ", len(a))

print("----------------------------------")

# Single Line

singleLine = "This is a single line string"
print(singleLine)

print("----------------------------------")

# Multi Line

multiLine = """
  This is a 
  multi line string
"""
print(multiLine)

print("----------------------------------")

#  Index of a string (including space)

x = "Hello World" # Index no . -> [0,1,2,....(length-1)] or [length, length-1, length-2,..., 1]

print(x[1]) # getting index no. 1 from left
print(x[-5]) # getting index no. 5 from right

print("----------------------------------")

#  Slicing a string (including space)

p = "Best tutorial"

# p[Start index: Ending index: Increment/Decrement]

print(p[0:2]) # Starting from 0 from left and ending at 2nd indexed position
print(p[0::2]) # Starting from 0 from left and ending at last indexed position with an increment of 2
print(p[0:7:1]) # Starting from 0 from left and ending at 6th indexed position with an increment of 1
print(p[-1::-1]) # Starting from 1 from right and ending at start position with a decrement of 1

print("----------------------------------")

# Using loop break a string

q = "Hi How are you"
length = len(q)

for m in range(length):
    print(q[m])

print("----------------------------------")

for n in range(length-1,-1,-1):
    print(q[n])

print("----------------------------------")

# String Comprehension

s="Hello"
d=[g for g in s]
print(d)