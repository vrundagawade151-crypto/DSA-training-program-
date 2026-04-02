for i in range(4):
    inp=ord(input("Enter a value in number,string,character,special characters"))
    if inp>=65 and inp<=90:
        print("it is a charcter in UPPER CASE")
    elif inp>=97 and inp<=122:
        print("it is a character in LOWER CASE")
    elif inp>=48 and inp<=57 :
        print("it is a number ")
    else:
        print("it is a special character")