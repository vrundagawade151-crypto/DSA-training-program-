#Extening property from one class to another class is called inheritance
#directly we are getting here reusability concept

# class College:
#     def college_name(self):
#         print("Modern College")

# class Student(College):
#     def student_info(self):
#         print("Name : Vrunda Gawade")
#         print("Branch : Mechanical")

# obj=Student()
# obj.college_name()
# obj.student_info()

#--------------------------------Multilevel------------------------------------------

# class College:
#     def college_name(self):
#         print("Modern College")

# class Student(College):
#     def student_info(self):
#         print("Name : Vrunda Gawade")
#         print("Branch : Mechanical")

# class Exam(Student):
#     def subject(self):
#         print("Subject1 : Design Engineering")
#         print("Subject2 : Math")
#         print("Subject3 : C-Language")

# obj=Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()

#---------------------------------------Multiple inheritance-----------------------------------

class SubjMarks:
    math=int(input("Enter paper marks of math : "))
    DE=int(input("Enter paper marks of design engineering"))
    c=int(input("Enter paper marks of c language : "))
    english=int(input("Enter paper marks of english : "))

class PracMarks:
    cpract=int(input("Enter practicals marks of c language : "))

class Result(SubjMarks,PracMarks):
    def total(self):
        if self.math>=40 and self.DE and self.c>=40 and self.english>=40 and self.cpract>=20:
            print("Pass")
        else:
            print("Fail")
obj=Result()
obj.total()