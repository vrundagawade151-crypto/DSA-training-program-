num=[-1,2,-3,4,5,-6]
neg=[]
pos=[]
final=[]
for i in num:
    if i<0:
        neg.append(i)
    else:
        pos.append(i)
print(pos)
print(neg)
for i,j in zip(neg,pos):
    final.append(i)
    final.append(j)

print(final)
