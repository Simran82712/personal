list=[1,2,3,1,9,1,2,1,9]
dict={}
maximum=-1;
dictKey=0
for i in list:
    count=0
    if i in dict.keys():
        dict[i]=dict[i]+1
    else:
        dict[i]=count+1

for i in dict.values():
    if i>maximum:
        maximum=i

for i in dict.keys():
    if dict[i]==maximum:
        dictKey=i

print(dictKey)

