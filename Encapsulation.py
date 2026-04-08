# _a(protected)             …………….if single underscore(_) then it protected
# __a(private)			    …………….if double underscore(__) then it private


#----------------------------------------public and private data members-----------------------------------------

# class Base:
#     def __init__(self):
#         print("Parent class constructor called")
#         self.a="Vrunda"     #Public member
#         self._b="Arya"      #Protected member
#         self.__c="Jyoti"    #Private member
#         # print(self.__c)
        

# class Derived(Base):
#     def __init__(self):
#         print("Calling private Members of base class:")
#         Base.__init__(self) #calling constructor of base class
#         # print(self.a)
#         # print(self._b)
#         # print(self.__c)

# obj1=Derived()
# print(obj1.a) #This is accessible
# print(obj1._b) #This is accessible
# print(obj1.__c) #This is not accessible

# print(obj1._Base__c) #This is accessible because we have given as _Base which is the name of Parent class


#----------------------------------------public and private data functions-----------------------------------------


class Rbi:
    def publicPolicy(self):             #parent class public method
        print("Check the public policy of RBI")

    def __privatePolicy(self):          #parent class private method
        print("There is some private policy which is not accessible for public")    

class Sbi(Rbi):
    def __init__(self):                 #Sbi child class constructor called first
        Rbi.__init__(self)              #Rbi parent class constructor called first
    
    def callingPublicMethod(self):      #child class public method
        print("\nInside child class")
        self.publicPolicy()             #calling child class public method

    def callingPrivateMethod(self):     #child class public method
        self.privatePolicy()            #calling parent class private method

# obj1=Sbi()
# obj1.callingPublicMethod()
# obj1.callingPrivateMethod()
# obj1.publicPolicy()
# obj1.__privatePolicy()

# obj2=Rbi()
# obj2.publicPolicy()
# obj2.__privatePolicy()

obj2=Rbi()
obj2.publicPolicy()
obj2._Rbi__privatePolicy()
