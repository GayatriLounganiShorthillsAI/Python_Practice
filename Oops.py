class computer:
        def __init__(self,cpu,ram):
                self.x = cpu
                self.y = ram
        def config(self):
                print("config is:" , self.x, self.y)


c = computer('i5', 19)
d = computer('Ryzen 3',6)
print(type(c))

# computer.config(c)
c.config()
d.config()
 