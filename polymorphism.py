# DUCK TYPING IN PYTHON
class Pycharm:
       def execute(self):
              print("compilling")
              print("running")
class Laptop:
        def code(self, ide):
              ide.execute()  

ide = Pycharm()

lap1 = Laptop()
lap1.code(ide)