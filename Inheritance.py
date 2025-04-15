# class A:
#        def feature1(self):
#               print("first")

#        def feature2(self):
#               print("second")

# # B is child class
# class B(A):
#        def feature3(self):
#               print("third")
#        def feature4(self):
#               print("fourth")
# class C(B):
#        def feature5(self):
#           print("fifth")    
# a = A()
# a.feature1()
# a.feature2()

# b1 = B()
# # B also inherits A 
# b1.feature2()

# #C->B->A
# c = C()
# c.feature1()


# class A:
#        def feature1(self):
#               print("first")

#        def feature2(self):
#               print("second")

# # B is child class
# class B:
#        def feature3(self):
#               print("third")
#        def feature4(self):
#               print("fourth")
# class C(A,B):
#        def feature5(self):
#           print("fifth")    
# a = A()
# a.feature1()
# a.feature2()


# #C->B->A
# c = C()
# c.feature5()

class A:
       def __init__(self):
              print("in A init")

       def feature1(self):
              print("first")

       def feature2(self):
              print("second")

# B is child class
class B(A):
       def __init__(self):
              print("in b init")
       def feature3(self):
              print("third")
       def feature4(self):
              print("fourth")
  
#  GO IN INIT OF B 
a = B() 

