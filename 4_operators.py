# Arithmetic Operators

x = 2
y = 5

print("Arithmetic Operators")
print("-------------------")
print(x + y) # This will give the addition of two numbers
print(x - y) # This will give the subtraction of two numbers
print(x * y) # This will give the product of two numbers
print(x / y) # This will give the division of two numbers
print(x % y) # This will give the remainder of two numbers
print(x ** y) # This will give the result of 'x' to the power of 'y'
print(y // x) # This will give the floor result

print()

# Comparison Operators

a = 2
b = 5

print("Comparison Operators")
print("-------------------")
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

print()

# Logical Operators

c = 4
d = 8

print("Logical Operators")
print("-------------------")
print(c > 3 and d < 7) # Returns TRUE if all are TRUE
print(c < 3 or d > 7) # Returns TRUE if any one is TRUE
print(not(c < 3)) # Returns the reverse result

print()

# Identity Operators

m = 4
n = 8

print("Identity Operators")
print("-------------------")
print(m is n) # Returns TRUE if both variables are the same object | Same as : m == n
print(m is not n) # Returns TRUE if both variables are not the same object | Same as : m != n

print()

# Membership Operators

string = "Hello"

print("Membership Operators")
print("-------------------")

print ('H' in string) # Returns TRUE if a sequence with the specified value is present in the object
print ('H' not in string) # Returns TRUE if a sequence with the specified value is not present in the object

# N.B.: This can be implement in 'list'/'tuple' also

print()

# Bitwise Operators
# All will be in 16 bits

p = 7
q = 5

print("Bitwise Operators")
print("-------------------")
print(bin(p))
print(bin(q))
print (p & q) # AND: Sets each bit to 1 if both bits are 1
print (p | q) # OR: Sets each bit to 1 if one of two bits is 1
print (p ^ q) # XOR: Sets each bit to 1 if only one of two bits is 1
print (~p) # NOT: Reverse all the bits (means : 1 to 0 and 0 to 1)
print (p<<1) # Zero fill left shift: Shift left by pushing zeros in from the right and let the leftmost bits fall off
print (q>>1) # Signed right shift: Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

print()

# Assignment Operators

string = "Hello"

print("Assignment Operators")
print("-------------------")

r = 5 # Assigned to x, same as x=5
r += 3 # Same as r = r + 3
r -= 3 # Same as r = r - 3
r *= 3 # Same as r = r * 3
r /= 3 # Same as r = r / 3
r %= 3 # Same as r = r % 3
r **= 3 # Same as r = r ** 3
r //= 3 # Same as r = r // 3
r &= 3 # Same as r = r&3
r |= 3 # Same as r = r | 3
r >>= 3 # Same as r = r >> 3
r <<= 3 # Same as r = r << 3
print(r := 3) # Same as r = 3 print(r)




