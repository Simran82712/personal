import math

lst=[('Simran',0),('Ankit',40),('Akash',65)]
marks=[]
for name,mark in lst:
    marks.append(mark)

average = sum(marks) / len(lst)
print (average)
for nam,mar in lst:
    if mar>average:
        print((nam,mar))

#find same for dictionary
dict={'Simran':100,'Vicky':0,'Ankit':99}
maximum=max(dict.values())


for key,value in dict.items():
     if value==maximum:
        print((key,value))

