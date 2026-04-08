#abstract method is a method which soes not have implementation in abstract method in abstract class

# from abc import ABC,abstractmethod
# class Help4code(ABC): #decorator
#     @abstractmethod 
#     def Placement(self):#abstract method
#         pass

#     @abstractmethod #decorator
#     def Training(self):#abstract method
#         pass

# class Vrunda(Help4code):
#     def Training(self):
#         print('C','C++','Java')
#     def Placement(self):
#         print("Java Placement")

# class Arya(Help4code):
#     def Training(self):
#         print('Python','Django')
#     def Placement(self):
#         print("Python Placement")

# class Jyoti(Help4code):
#     def Training(self):
#         print('Machine Learning')
#     def Placement(self):
#         print("Data Science placement")

# obj1=Vrunda()
# obj2=Arya()
# obj3=Jyoti()

# obj1.Training()
# obj1.Placement()

# obj2.Training()
# obj2.Placement()

# obj3.Training()
# obj3.Placement()

from abc import ABC,abstractmethod
class IRCTC(ABC): #decorator
    @abstractmethod 
    def bookTicket(self):#abstract method
        pass

class MakeMyTrip(IRCTC):

    def bookTicket(self):
        print("===============================================")
        print("     Welcome To makemytrip.com   ")
        source=input("Enter a source station name")
        destination=input("Enter destination name")
        date=input("Enter date")
        print("===============================================")

class GoIbibo(IRCTC):

    def bookTicket(self):
        print("===============================================")
        print("     Welcome To GoIbibo   ")
        source=input("Enter a source station name")
        destination=input("Enter destination name")
        date=input("Enter date")
        print("===============================================")
        
class RedBus(IRCTC):

    def bookTicket(self):
        print("===============================================")
        print("     Welcome To RedBus   ")
        source=input("Enter a source station name")
        destination=input("Enter destination name")
        date=input("Enter date")
        print("===============================================")

obj1=MakeMyTrip()
obj2=GoIbibo()
obj3=RedBus()

obj1.bookTicket()
obj2.bookTicket()
obj3.bookTicket()
