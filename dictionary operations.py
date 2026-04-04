# mydict={
#     101:"prashant",
#     102:"ashish",
#     "103":"mohini",
#     "104":"trivani",
#     101:"ashish",                #updates 101:prashnt -> ashish
#     104:"ashish"
# }
# print(mydict)

# a=mydict[102]                  #getting value by id
# print(a)

# mydict[102]="peter"
# print(mydict)

# for x in mydict:               #prints only keys
#     print(x)

# for x in mydict.values():        #prints only values
#     print(x)

# for x,y in mydict.items():        #prints keys and values side by side
#     print(x,y)

# mydict["mobile_number"]=7517916006
# print(mydict)

# a={(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])

# a={'a':1,'b':2,'c':3}
# print(a['a','b'])

# arr={}
# arr[1]=1
# arr['1']=2
# arr[1]+=1

# sum=0
# for k in arr:
#     sum+=arr[k]
# print(sum)

# my_dict={}
# my_dict[(1,2,4)]=8
# my_dict[(4,2,1)]=10
# my_dict[(1,2)]=12
# sum=0
# for k in my_dict:
#     sum+=my_dict[k]
# print(sum)
# print(my_dict)

# box={}
# jars={}
# crates={}
# box['biscuit']=1
# box['cake']=3
# jars['jam']=4
# crates['box']=box
# crates['jars']=jars
# print(len(crates[box]))

# dict={'c':97,'a':96,'b':98}
# r=dict
# print(id(r))
# print(id(dict))
# print(id(r)==id(dict))

rec={"Name":"python","age":"20"}
id1=id(rec)
del rec
rec={"Name":"python","age":"20"}
id2=id(rec)
print(id1)
print(id2)
print(id1==id2)