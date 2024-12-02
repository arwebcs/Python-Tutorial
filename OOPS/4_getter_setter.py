class Student:
    def __init__(self):
        self.__name = ""
    def getName(self):
        return self.__name
    def setName(self,nm):
        self.__name=nm

stdObj = Student()
stdObj.setName("Student")
print(stdObj.getName())