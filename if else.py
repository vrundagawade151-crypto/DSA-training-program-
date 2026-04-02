# username =input("enter a username")
# password=input("Enter a password")
# if username==password:
#     print("Login successful")
# else:
#     print("invalid Credentials")

phy = int(input("Enter Marks of physics"))
chem = int(input("Enter marks of chemistry"))
mat=int(input("Enter marks of maths"))
gender=input("Enter gender male or female")

total=phy+chem+mat
percent=(total/300)*100

if percent>=60 and gender=="male":
    print("Eligible for data entry job")

else:
    print("not Eligible for data entry job")