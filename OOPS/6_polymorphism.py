# Overloading

print("Overloading")

class Course:
    def displayCourse(self, courseName=''):
        print("Welcome",courseName)

obj =Course()
obj.displayCourse()
obj.displayCourse("Python")
print()

print("Example of overloading")

class Area:
    def findArea(self,a=None, b=None):
        if(a!=None and b!=None):
            print("Area of Rectangle: ", (a*b))
        elif a!=None:
            print("Area of square: ", (a * a))
        else:
            print("Invalid")

obj = Area()
obj.findArea()
obj.findArea(5)
obj.findArea(7,8)

print("-----------------------------------------------")

# Overriding

print("Overriding")

class Employee:
    def displayEmployeeInfo(self):
        print("Employee")
class Manager(Employee):
    def displayEmployeeInfo(self):
        super().displayEmployeeInfo()
        print("Manager")

obj =Manager()
obj.displayEmployeeInfo()

print()

print("Example of overriding")

class A:
    def showData(self):
        print('I am in A')
class B(A):
    def showData(self):
        super().showData()
        print('I am in B')

obj = B()
obj.showData()