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
 

class Computer:
        def __init__(self):
                self.name = "name"
                self.age = 20

        def update(self):
                self.age = 90
                self.name = "new name"  
        def compare(self, d):
                if self.age == d.age :
                        return True
                else:
                        return False

c = Computer()
d = Computer()

d.name = "riya"
d.age = 9

c.update()

if c.compare(d):
        print("they are same")
else:
        print("they are not same")


print(id(c))
print(c.name, c.age)
print(d.name, d.age)
