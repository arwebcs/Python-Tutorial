# Single Level Inheritance
print("Single Level Inheritance")

class A:
    def displayA(self):
        print("Welcome to A")

class B(A):
    def displayB(self):
        print("Welcome to B")

objB=B()
objB.displayB()
objB.displayA()

print("--------------------------------------------------")

# Multi Level Inheritance

print("Multi Level Inheritance")

class A1:
    def displayA1(self):
        print("Welcome to A1")

class B1(A1):
    def displayB1(self):
        print("Welcome to B1")
class C1(B1):
    def displayC1(self):
        print("Welcome to C1")

objC1=C1()
objC1.displayC1()
objC1.displayB1()
objC1.displayA1()

print("--------------------------------------------------")

# Multiple Inheritance

print("Multiple Inheritance")

class A2:
    def displayA2(self):
        print("Welcome to A2")
class B2:
    def displayB2(self):
        print("Welcome to B2")
class C2(A2,B2):
    def displayC2(self):
        print("Welcome to C2")

objC2=C2()
objC2.displayC2()
objC2.displayB2()
objC2.displayA2()