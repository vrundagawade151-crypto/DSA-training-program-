val1=int(input("Enter the first number: "))
val2=int(input("Enter the second number: "))

print("Before swapping:", val1, val2)

val1=val1+val2 # val1=12
val2=val1-val2 # val2=12-2=10
val1=val1-val2 # val1=12-10=2

print("After swapping:", val1, val2)
