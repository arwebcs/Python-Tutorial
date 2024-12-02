class DemoClass :
    a =10
    def __init__(self):
        print("Constructor")
    def sum(self):
        self.c = self.a + self.a
        return self.c
    def show(self):
        print("Welcome to Python")
    def showArg(self, a, b):
        print(a,b)

demoObj = DemoClass()
print(demoObj.sum())
demoObj.show()
demoObj.showArg(40,50)