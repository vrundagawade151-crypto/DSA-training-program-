#Polymorphism means giving different operations to same same function name.

#----------------------------------------------------------------
# class Principal:
#     def role(self):
#         print("I am managing all activity of college")
# class Dean:
#     def role(self):
#         print("Dean-I am decision taking person")
# class Hod:
#     def role(self):
#         print("Hod-I have a responsibilty of teachersa and students")
# class Faculty:
#     def role(self):
#         print("Faculty-I have to complete syllabus successfully")

# def func(obj):
#     obj.role()
# campus=[Principal(),Dean(),Hod(),Faculty()]
# for obj in campus:
#     func(obj)


#-------------------------overloading------------------------------------
# Python only supports operator overloading
# Python does not support method overloading and constructor operloading


# this is method overloading which does not support python  
# in method overloading it considers last function and do call 1st


# This code does not runs
# class Arithmetic:
#     def add(self,a):
#         print(self.a)
#     def add(self,a,b):
#         print(self.a+self.b)
#     def add(self,a,b,c):
#         print(self.a+self.b+self.c)

# obj=Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)


#this code runs
# class Arithmetic:
#     def add(self,a=None,b=None,c=None):
#         if a!=None and b!=None:
#             print(a+b)
#         elif a!=None and b!=None and c!=None:
#             print(a+b+c)
#         else:
#             print("Enter atleast two argument")
# obj=Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)

#------------------------------------------Constructor overloading-------------------------
# This code does not runs
# class Arithmetic:
#     def __init__(self):
#         print("There is no argument")
#     def __init__(self,a):
#         print("passing one argument")
#     def __init__(self,a,b):
#         print("passing two argument")

# obj=Arithmetic()
# obj=Arithmetic(10)
# obj=Arithmetic(2,2)

#------------------------overridding----------------------------------------
#python supports both constructor and method overriding
#using super() we can call parent class method in child class


# method overriding
# class Rbi:
#     def home_loan(self):
#         print("Home Loan = 7.5")
#     def car_loan(self):
#         print("Car Loan 8%")

# class Sbi(Rbi):
#     def home_loan(self):
#         super().home_loan()
#         print("Sbi provide Home Loan = 6.5")

# obj=Sbi()
# obj.home_loan()
# obj.car_loan()


# constructor overloading
# class Father:
#     def __init__(self):
#         print("I am already at breakfast table ")

# class Child(Father):
#     def __init__(self):
#         super().__init__()
#         print("Child i will be late for breakfast")

# obj=Child()
