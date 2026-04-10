# recursion uses stackk 
# we use recursion especially in the cases we know that a problem can be divided into similar sub problems

#---------------------------------------------------------------------------------------------------------------------------

# factorial

# def factorial(num):
#     if num>=1:
#         return num*factorial(num-1)
#     return 1
    
# print(f"Factorial of 5 is ",factorial(5))

#---------------------------------------------------------------------------------------------------------------------------

# palindrome

# def isPalindrome(strng):
#     if len(strng)==0:
#         return True
#     if strng[0]!=strng[len(strng)-1]:
#         return False
#     return isPalindrome(strng[1:-1])

# print(isPalindrome("awesome"))
# print(isPalindrome("foobar"))
# print(isPalindrome(""))
# print(isPalindrome("tacocat"))

#---------------------------------------------------------------------------------------------------------------------------

# power

# def power(base,exponent):
#     if exponent==0:
#         return 1
#     return base*power(base,exponent-1)
# print(power(2,0))
# print(power(2,2))
# print(power(2,4)) 

#---------------------------------------------------------------------------------------------------------------------------

#capitalize first

# def capitalizeFirst(arr):
#     result=[]

#     if len(arr)==0:
#         return result
#     result.append(arr[0][0].upper()+arr[0][1:])
#     return result+capitalizeFirst(arr[1:])

# print(capitalizeFirst(['car','taco','banana']))

#---------------------------------------------------------------------------------------------------------------------------

#product of array

# def productOfArray(arr):
#     if len(arr)==0:
#         return 1
#     return arr[0]*productOfArray(arr[1:])

# print(productOfArray([1,2,3]))
# print(productOfArray([1,2,3,4]))

def fib(num):
    if (num<2):
        return num
    return fib(num-1)+fib(num-2)

print(fib(4))

