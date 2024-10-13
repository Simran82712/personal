import heapq

lst=[3,0,9,1,8,7]
max=0
for i in lst:
    if i > max:
      max=i
print(heapq.nlargest(4,lst)[-1])
print(max)