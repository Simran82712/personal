#
Input='bbbbcccaaaj'
Output=[4,3,2,1]

n=len(Input)
# count=1
# lst=[]
# for i in range(n-1):
#     if(Input[i]==Input[i+1]):
#         count=count+1
#
#     else:
#         lst.append(count)
#         count=1
# lst.append(count)
# print(lst)

dict={}
count=0
for i in Input:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1

print(list(dict.values()))