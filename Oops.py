# class computer:
#         def __init__(self,cpu,ram):
#                 self.x = cpu
#                 self.y = ram
#         def config(self):
#                 print("config is:" , self.x, self.y)


# c = computer('i5', 19)
# d = computer('Ryzen 3',6)
# print(type(c))

# # computer.config(c)
# c.config()
# d.config()
 

# class Computer:
#         def __init__(self):
#                 self.name = "name"
#                 self.age = 20

#         def update(self):
#                 self.age = 90
#                 self.name = "new name"  

#         def compare(self, d):
#                 if self.age == d.age :
#                         return True
#                 else:
#                         return False

# c = Computer()
# d = Computer()

# d.name = "riya"
# d.age = 9

# c.update()

# if c.compare(d):
#         print("they are same")
# else:
#         print("they are not same")


# print(id(c))
# print(c.name, c.age)
# print(d.name, d.age)


# -------Types of variable

# class Car:
#  #  ----- class variable and static variables are same
#         wheels = 4  #class variable , class namespace
#         def __init__(self, mil, company):  #instance variable, instance namespace
#                 self.mil=mil
#                 self.company=company

# c = Car(20, "bmw")
# d = Car(30, "range rover")

# c.mil=0
# d.company="maruti"
# print(c.mil, c.wheels)
# print(d.company, c.wheels, d.wheels)


# ---------Types of method
# instance variable -> self keyword
# class variable -> cls keyword

class Student:
        school = 'Tagore public school'
        def __init__(self,a,b,c):
                self.a = a
                self.b = b
                self.c = c
        def avg(self):
                return (self.a+ self.b+self.c)/3
        def get_a(self):
                return self.a
        def set_a(self, val):
                self.a = val

        @classmethod   #decorators
        def getSchool(cls):
                return cls.school
        
        @staticmethod
        def info():
                print("this is student class...in abc module")
c = Student(34,34,34)

print(c.avg())

# both can be used
print(c.getSchool())
print(Student.getSchool())
print(c.info())