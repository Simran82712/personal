l=1
lst=[0,0,1,1,1,2,2,2,2,3,3,4,4,5,5]

for r in range(1,len (lst)):
    if lst[r]!=lst[r-1]:
        lst[l]=lst[r]
        l=l+1
print(l,lst)
