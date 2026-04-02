# math = 50
# name =" Vrunda"
# pi= 3.14
# result=True
# print(type(math))
# print(type(name))
# print(type(pi))
# print(type(result))                       #returns the type of the variable
# print(id(math))
# print(id(name))
# print(id(pi))
# print(id(result))                           #returns the memory address of the variable
# math = 50
# chem = 60
# print(id(math))
# print(id(chem))

# print(2+2)
# print("2"+"2")
# val1=input("Enter the first number: ")
# val2=input("Enter the second number: ")
# print(val1+val2)                               #concatenation of strings
# print(int(val1)+int(val2))                     #addition of integers
            
# print(complex(3))
# print(complex(True))
# print(complex(False))
# print(complex("3.14"))
# print(complex("4"))
# print(complex('5'))
# print(complex('5.6'))
# print(complex(5,-3))
# print(complex(True,False))

# print(bool(0))
# print(bool(True))
# print(bool(False))
# print(bool("3.14"))
# print(bool("0"))
# print(bool('5'))
# print(bool(0.0))
# print(bool(5-3j))
# print(bool())

    
    
#we cannot convert complex value to int 
#we cannot convert floating point value to string
#cant convert string to int


val1=int(input("Enter the first number: "))
val2=int(input("Enter the second number: "))
print("Before swapping:", val1, val2)

val1=val1+val2 # val1=12
val2=val1-val2 # val2=12-2=10
val1=val1-val2 # val1=12-10=2

print("After swapping:", val1, val2)