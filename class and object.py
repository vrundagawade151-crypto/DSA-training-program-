# class Student:
#     roll_no=101 #data member

#     def studentData(self): #member function
#         print("Student Information")

# obj=Student()  #object created
# print(obj.roll_no) #calling a data member
# obj.studentData() #calling a member function    

#-------------------------------------Constructor---------------------------------------------------------------------

# class Demo:
#     def __init__(self):
#         print("I am a constructor")

#     def msg(self):
#         print("Hello class")

# obj=Demo()
# obj.msg()

#----------------------------------------------------------------------------------------------------------

# class Hod:
#     def __init__(self):
#         self.name='Vrunda Gawade'
#         self.age=21
#         self.empid=3212

#     def info(self):
#         print("My name is : ",self.name)
#         print("My age is : ",self.age)
#         print("My emp id is : ",self.empid)

# obj=Hod()
# obj.info()

#-------------------------------------- Parameterize constructor--------------------------------------------------------------

# class Hod:
#     def __init__(self,name,age,rollno):
#         self.name=name
#         self.age=age
#         self.rollno=rollno

#     def show(self):
#         print("My name is ",self.name)
#         print("My age is : ",self.age)
#         print("My rollno is : ",self.rollno)

# obj=Hod('Vrunda',21,19)
# obj.show()

#----------------------------------- Types of variable -------------------------------------------------------------

# instance variable    =   creates a seperate memory for 1 variable 

# class New:
#     def __init__(self):
#         self.a=10

# obj1=New()
# obj2=New()
# obj3=New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# obj1.a=20
# print()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

#  declaring instance variable "inside using self , function using self and outside using obj" a class by using object

# class Student:
#     def __init__(self):
#         self.s_name="vrunda"
#         self.s_rollno=19
#     def getdata(self):
#         self.s_mb=7517916006

# obj=Student()
# obj.getdata()
# del obj.s_mb                  #delete instance variable
# obj.s_branch="CS"             #adding instance variable using obj
# print(obj.__dict__)


#  declaring static variable a class by using object

# class Student():
#     a=10
#     def __init__(self):
#         self.b="Vrunda"

# obj=Student()
# obj1=Student()
# obj2=Student()
# print(obj.a)
# print(obj1.a)
# print(obj2.a)
# Student.a=50
# print()
# print(obj.a)
# print(obj1.a)
# print(obj2.a)

#-----------------------------------------------------------------------------------------------------

# class Student:
#     def __init__(self,name,rollno,mob):
#         self.name=name
#         self.rollno=rollno
#         self.mob=mob
    
#     def display(self):
#         print(self.name," ",self.rollno," ",self.mob)

# stud=Student("prashant",1001,6464646)
# stud.display()

#-----------------------------------------------------------------------------------------------------

class Student:

    @staticmethod
    def get_personal_details(firstname,lastname):
        print("your personal details=",firstname,lastname)

    @staticmethod
    def contact_detail(mobil_no,rollno):
        print("Your contact detail=",mobil_no,rollno)

Student.get_personal_details("Vrunda","Gawade")
Student.contact_detail(7517916006,1001)
