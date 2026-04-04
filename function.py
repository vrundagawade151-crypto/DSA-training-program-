# def msg(): #called function
#     print("hello world")

# msg() #calling function

# def arithmetic():
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     add=a+b
#     sub=a-b
#     mul=a*b
#     div=a//b
#     return add,sub,mul,div
# result=arithmetic()
# print(result)

#positional argument
# def login(username,password):
#     if username==password:
#         print("login successful")
#     else:
#         print("invalid credentials")


# username=input("enter username:")
# password=input("enter password:")
# login(username,password)

#keyword argument
# def login(username,password):
#     if username==password:
#         print("login successful")
#     else:
#         print("invalid credentials")


# username=input("enter username:")
# password=input("enter password:")
# login(username="admin",password="admin")

#default argument
# def cityName(city="goa"):
#     print(city)

# cityName("delhi")
# cityName("nagpur")
# cityName()

#variable name argument

# def nameOfCity(*city):
#     print("city name 's=",city)

# nameOfCity("goa","nagpur","mumbai")


#------------------------------------------------------------------------------------------------

# import sys

# def add():
#     val1=int(input("Enter the value of val1 : "))
#     val2=int(input("Enter the value of val2 : "))
#     print("Addition=",val1+val2)

# def sub():
#     val1=int(input("Enter the value of val1 : "))
#     val2=int(input("Enter the value of val2 : "))
#     print("Subtraction=",val1-val2)

# def mul():
#     val1=int(input("Enter the value of val1 : "))
#     val2=int(input("Enter the value of val2 : "))
#     print("Multiplication=",val1*val2)

# def div():
#     val1=int(input("Enter the value of val1 : "))
#     val2=int(input("Enter the value of val2 : "))
#     print("Division=",val1/val2)



# while True:
#     print("1. Addition")
#     print("2. Substraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")
#     choice=int(input("Enter a choice : "))

#     if choice==1:
#         add()
#     elif choice==2:
#         sub()
#     elif choice==3:
#         mul()
#     elif choice==4:
#         div()
#     else:
#         sys.exit()

# 1.rstrip()==> To remove spaces at right hand side
# 2.lstrip()==> To remove spaces at left hand side
# 3.strip()==> To remove spaces at both side

# programming = input("enter your programming language : ")
# p_name=programming.strip()
# if p_name=='Python':
#     print(p_name)
# elif p_name=='Java':
#     print(p_name)
# elif p_name=='CPP':
#     print(p_name)
# else:
#     print("Wrong Programming name")