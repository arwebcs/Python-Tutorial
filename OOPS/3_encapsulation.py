# Private : __<variable/function>

class Employee:
    __name="Employee" #private
    def __init__(self):
        print(self.__name)
        self.__displayinfo()
    def __displayinfo(self): #private
        print("Welcome")

stdObj = Employee()

print(stdObj.__name)