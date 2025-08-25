# parent class
class Person():

    # __init__ is knnown as constructorr
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        #invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

#creation of an object variable or instance
a = Employee('penguin', 202154550, 15000, "intern")

# calling a function of the class person using its instance
a.display()