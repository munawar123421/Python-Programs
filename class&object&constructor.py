print("<____________Class & Object & Constructor____________>")
"""class Student:       #class is the blueprint for reusability and remove redundancy
    def __init__(self):  #default constructor automatically calls when object of class is created
        print("this is my constructor for student class")
    name="Munawar"
    age=19
s=Student()          #objects are used for accessingt the members in class
print(s.name)
print(s.age)
s1=Student()
print(s1.name)
print(s1.age)"""

"""class Car:
    name="lamborghini"
    model=2020
    tyre=4
car1=Car()
print("specifications of car :",car1.name,car1.model,car1.tyre)"""

"""class Mobile:
    def __init__(self):
        print(self)
        print("mobile class default constructor")
    name="SAMSUNG S24ULTRA"
    price=500000
mob1=Mobile()
print(mob1)
print(mob1.name)
print(mob1.price)"""

"""class Student:
    def __init__(self,fullname,fullage):  #parametarized constructor which takes two parameter
        self.name=fullname
        self.age=fullage
        print("This is my default constructor for student class")
std1=Student("khani",19)
print(std1.name)
print(std1.age)
std2=Student("mudasir",23)
print(std2.name)
print(std2.age)"""

class Student:
    def __init__(self):  #parametarized constructor which takes two parameter
        print("This is my default constructor for student class")
    def welcome(self):   #member function in class
        print("welcome student")
    def hello(self):
        print("hello students ap kasa hnnn")
std1=Student()
print(std1.welcome())
print(std1.hello())

#WAF NO.1
class Student:
    def __init__(self,name,marks_1,marks_2,marks_3):
        self.name=name
        self.marks_1=marks_1
        self.marks_2=marks_2
        self.marks_3=marks_3
        print(name)
    def average_std(self):
        print(self.name)
        sum=self.marks_1+self.marks_2+self.marks_3
        avg=sum/3
        print("average of marks passed as a parameter :",avg)
std1=Student("munawar",90,56,77)
std1.average_std()"




