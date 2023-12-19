#oop is a software development paradigm 

# #Ex1
# #this example to definetion about oop
# class customer :
#     pass 
# c1 = customer() #object in class 
# print(c1)

# #Ex2
# class customer :
#     def identify (self, name):
#         print("my name is "+ name)
# obj = customer()
# obj.identify("wing")

# # Ex3
# class Firstclass():
#     def dataset(self, value):
#         self.data = value
#     def display (self):
#         print(self.data)
# obj = Firstclass()
# obj1 = Firstclass()

# print(obj)
# print(obj1)
# print(isinstance(obj, Firstclass))
# obj.dataset("tofee")
# obj1.dataset(15)
# obj.display()
# obj1.display()

# #Ex4
# class person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def display(self):
#         print(self.name, self.age)

# class young (person):
#     def __init__(self, name, age, dob):
#         self.dob = dob
#         super(). __init__(name, age)
    
#     def display(self):
#         print(self.name, self.age, self.dob)

# obj = young("nasr", 20, 3)
# obj.display()
    
# #Ex4
# # Python example to show the working of multiple
# # inheritance

# class Base1(object):
#  	def __init__(self):
# 		 self.str1 = "Geek1"
# 		 print("Base1")


# class Base2(object):
#  	def __init__(self):
# 		 self.str2 = "Geek2"
# 		 print("Base2")


# class Derived(Base1, Base2):
#  	def __init__(self):

# 		# Calling constructors of Base1
# 		# and Base2 classes
# 		 Base1.__init__(self)
# 		 Base2.__init__(self)
# 		 print("Derived")

#  	def printStrs(self):
# 		 print(self.str1, self.str2)


# ob = Derived()
# ob.printStrs() 
        
# #Ex5
# # A Python program to demonstrate multilevel 

# # inheritance 

# class Base(object):

# 	# Constructor
# 	def __init__(self, name):
# 		self.name = name

# 	# To get name
# 	def getName(self):
# 		return self.name


# # Inherited or Sub class (Note Person in bracket)
# class Child(Base):

# 	# Constructor
# 	def __init__(self, name, age):
# 		Base.__init__(self, name)
# 		self.age = age

# 	# To get name
# 	def getAge(self):
# 		return self.age

# # Inherited or Sub class (Note Person in bracket)


# class GrandChild(Child):

# 	# Constructor
# 	def __init__(self, name, age, address):
# 		Child.__init__(self, name, age)
# 		self.address = address

# 	# To get address
# 	def getAddress(self):
# 		return self.address


# # Driver code
# g = GrandChild("Geek1", 23, "Noida")
# print(g.getName(), g.getAge(), g.getAddress())        

"""
Public Access Modifier: 
    
    All data members and member functions of a class are public by default.
"""
# #public class
# class AboSalah():
#     def __init__(self, name, idNumber):
#         self.name = name
#         self.idNumber = idNumber
#     def display(self):
#         print(self.name, self.idNumber)

# obj = AboSalah("Ahmed", 72417)
# print("Name: ", obj.name)
# print("ID: ", obj.idNumber)
# obj.display()

"""
Protected Access Modifier:
    The members of a class that are declared protected are only accessible to a class derived 
    from it. Data members of a class are declared protected by adding a single underscore ‘_’ 
"""
# #protected class
# class Student:
#     _name = None
#     _roll = None
#     _branch = None
    
#     def __init__(self, name, roll, branch):
#         self._name = name
#         self._roll = roll
#         self._branch = branch
        
#     def _display(self):
#         print("Roll: ", self._roll)
#         print("Branch: ", self._branch)

# class Geek(Student):
#     def __init__(self, name, roll, branch):
#         super(). __init__(name, roll, branch)
        
#     def display(self):
#         print("Name: ", self._name)
#         self._display()
# obj = Geek("tofee", 26, 7000)
# obj.display()

"""
Private Access Modifier:
    The members of a class that are declared private are accessible within the class only, 
    Data members of a class are declared private by adding a double underscore ‘__’
"""
# #private class
# class Geek ():
#     #privte members
#     __name = None
#     __age = None
#     __salary = None
    
#     #constructor
#     def __init__(self, name, age, salary):
#         self.__name = name
#         self.__age = age
#         self.__salary = salary
        
#     def __display (self):
#         print(self.__name, self.__age, self.__salary)
#     def accessPrivte (self):
#         self.__display()
    
# obj = Geek("ali", 10, 600)
# obj.accessPrivte()

# #Conditional Inheritance in Python
# class A(object):
#     def __init__(self, x):
#         self.x = x
#     def getx(self):
#         return self.x
# class B(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def getsum(self):
#         return self.x + self.y
# class c (A):
#     def isA (self):
#         return True
#     def isB (self):
#         return False
# class d (B):
#     def isA(self):
#         return False
#     def isB (self):
#         return True
# def get_c (cond):
#         if cond:
#             return c(1)
#         else:
#             return d(1, 2)
# obj = get_c(True)
# print (obj.isA())
# print(obj.isB())

# obj2 = get_c(False)
# print(obj2.isA())
# print(obj.isB())        

# #Ex2
# class A(object):
#     def __init__(self, x):
#         self.x = x
#     def getx(self):
#         return self.x
# cond = True
# class C(A if cond else object):
#     def IsA (self):
#         return True
# obj = C(1)
# print(obj.IsA())

# # Python program to show that the variables with a value 
# # assigned in class declaration, are class variables
# class student (object):
#     stream = 'lol'
#     def __init__(self, name, roll):
#         self.name = name 
#         self.roll = roll
# a = student("ali", 2)
# b = student("miral", 4)

# print(a.stream) 
# print(b.stream) 
# print(a.name) 
# print(b.name) 
# print(a.roll) 
# print(b.roll)      
# print (student.stream) 
# # To change the stream for all instances of the class we can change it 
# # directly from the class
# student.stream = 'marmar'
# print(a.stream) 
# print(b.stream)

# #explain overriding and overloading
# #Ex for overriding
# class Parent(): 
# 	
# 	# Constructor 
# 	def __init__(self): 
# 		self.value = "Inside Parent"
# 		
# 	# Parent's show method 
# 	def show(self): 
# 		print(self.value) 
# 		
# # Defining child class 
# class Child(Parent): 
# 	
# 	# Constructor 
# 	def __init__(self): 
# 		self.value = "Inside Child"
# 		
# 	# Child's show method 
# 	def show(self): 
# 		print(self.value) 
# 		
# 		
# # Driver's code 
# obj1 = Parent() 
# obj2 = Child() 

# obj1.show() 
# obj2.show()

# #Ex for overloading
# from multipledispatch import dispatch

# # passing one parameter


# @dispatch(int, int)
# def product(first, second):
# 	result = first*second
# 	print(result)

# # passing two parameters


# @dispatch(int, int, int)
# def product(first, second, third):
# 	result = first * second * third
# 	print(result)



# @dispatch(float, float, float)
# def product(first, second, third):
# 	result = first * second * third
# 	print(result)


# product(2, 3) 

# product(2, 3, 2) 

# product(2.2, 3.4, 2.3) 
