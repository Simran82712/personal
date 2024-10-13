l=[1,1,2,0,1,2,0,0]  #00011122
count_0=0
count_1=0
count_2=0
for i in l:
    if i==0:
        count_0=count_0+1
    elif i==1:
        count_1+=1
    elif i==2:
        count_2+=1



for i in range(0,count_0):
    l[i]=0
for i in range(count_0,count_0+count_1):
    l[i]=1
for i in range(count_0+count_1,count_0+count_1+count_2):
    l[i]=2
print(l)