
#generate the code to convert given string into below given output str="aaabbbcccc"
#a3b3c4

str1="aaabbbcccc"
output=""
dict={}

for i in str1:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1

for key,value in dict.items():
    output+=key+str(value)
print(output)
    