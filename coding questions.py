# dict1={"x":20,"y":10,"z":30}
# min_key,min_value=min(dict1.items())
# print({min_key})

#-------------------------------------------------------------------------------

# mydict={
#     101:"prashant",
#     "professional":"developer",
#     "empid":1001
# }

# mydict.pop(101)
# print(mydict)

#-------------------------------------------------------------------------------

#************_________________pattern printing numericals_________________***************

# for i in range(1,4):                                        1 1 1
#     for j in range(1,4):                                    2 2 2
#         print(i,end=" ")                                    3 3 3
#     print()

# n=int(input("enter number"))                                1
# for i in range(1,n+1):                                      1 2
#     for j in range(1,1+i):                                  1 2 3
#         print(j,end=" ")                                    1 2 3 4
#     print()                                                 1 2 3 4 5

# n=int(input("enter number of rows"))                        A
# for i in range(1,n+1):                                      B B
#     for j in range(1,1+i):                                  C C C
#         print(chr(64+i),end=" ")                            D D D D
#     print()                                                 E E E E E

# n=int(input("enter number of rows"))      
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print("*",end="")
#     print()

# n=int(input("enter number of rows"))      
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(n+2-i,end="")
#     print()

import time
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        time.sleep(2)
        print("*",end=" ")
    print()