# a=int(input("enter umber 1: "))
# b=int(input("enter number 2: "))
# c=int(input("enter number 3"))

# if a>b:
#     if a>c:
#         print(a," is greater")
#     else:
#         print(c," is greater")
# else:
#     if b>c:
#         print(b," is greater")
#     else:
#         print(c," is greater")

day=input("Enter day of week ")

if day!="sunday" or day!="SUNDAY" or day!="Sunday"or day!="saturday" or day!="SATURDAY" or day!="Saturday":
    print("working day")
else:
    print("Holiday")