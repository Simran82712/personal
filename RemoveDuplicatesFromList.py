lst=[1,2,3,1,3,2,2,2,4,5,1,3]
result=[]
n=len(lst)
for i in lst:
        if i not in result:
            result.append(i)

print(result)

#find reverse of a number without using string
num=12345
rev=0
while num!=0:
    rev=rev*10+num%10
    num=num//10

print(rev)