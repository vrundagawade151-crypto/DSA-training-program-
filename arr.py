arr=[3,3,4,2,4,4,2,4,4]
n=len(arr)
val=[]

for i in arr:
    if arr.count(i)>=n/2:
        val=i

print(val)

