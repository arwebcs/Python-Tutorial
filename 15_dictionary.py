# Dictionaries are like objects

# Method 1
course = {"course_name":"Python", "course_price":"Rs. 8000", "course_duration":"3 months"}
print(type(course), course)

# Method 2
val = dict(name='python', fees=8000)
print(type(val), val)

print("--------------------------------------------------")

# Iterate dictionary

print("Iterate dictionary")
for n in course:
    print(n, " ", course[n])

print("--------------------------------------------------")

# Get value
print("Get value of each key")
print(course['course_price'])
print(course.get('course_name'), course.get('course_price'), course.get('course_duration'))

print("--------------------------------------------------")

# Get all the keys in a list
print("Get all the keys in a list")
print(course.keys())

print("--------------------------------------------------")

# Get all the values in a list
print("Get all the values in a list")
print(course.values())

print("--------------------------------------------------")

# Get all the keys and values in a tuple within a list
print("Get all the values in a tuple")
print(course.items())

print("--------------------------------------------------")

for a in course.keys():
    print(a)

print()
for a in course.values():
    print(a)

print()
for a,b in course.items():
    print(a, b)

print("--------------------------------------------------")

# Some functions

print("Insert a property")
course['description']='This is PHP Course'
print(course)
print()
print("Update a property")
course.update({'course_name':'PHP'})
print(course)
print()
print("Update a property if exists, else insert")
course['description']='This is PHP Courses'
print(course)
print()
print("Delete a property")
del course['course_duration']
print(course)
print()
print("Pop a property and return the popped property")
t= course.pop("course_price")
print(t, " ",course)
print()
print("Clear the dictionary")
course.clear()
print(course)

print("--------------------------------------------------")

# Nested Dictionary

print("Nested Dictionary")

employee={
    'john':{'experience':'2 years', 'salary':15000},
'jack':{'experience':'3 years', 'salary':17000},
'alice':{'experience':'8 years', 'salary':51000}
}

print(employee)
print(employee['john'])
print(employee['jack']['experience'])
print(employee.keys())
print(employee.values())
print(employee.items())

for k,v in employee.items():
    print(k, " ", v)
