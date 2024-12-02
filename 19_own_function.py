# Simple function

print("Simple function")

def hello():
    print("Hello World")
hello()

print("-----------------------------------------------")

# Function with arguments

print("Function with arguments")

def add(a,b):
    print(a+b)

add(5,6)

print("-----------------------------------------------")

# Function with return type

print("Function with return type")

def add(a,b):
    return a+b

print(add(4,7))

print("-----------------------------------------------")

# Function with default value

print("Function with default value")

def add(a,b=4):
    return a+b

print(add(2))