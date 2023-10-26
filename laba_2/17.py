class Employee:
    __name = None
    __salary = None
    __age = None

    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getAge(self):
        return self.__age

    def setName(self, name):
        self.__name = name

    def setSalary(self, salary):
        self.__salary = salary

    def setAge(self, age):
        self.__age = age

employee = Employee('Anton', 500, 20)

employee.setName('Petr')
employee.setSalary('300')
employee.setAge(34)

print(employee.getName())
print(employee.getSalary())
print(employee.getAge())

