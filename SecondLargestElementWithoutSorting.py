lst=[3,0,9,1,8,7]
# maxi=lst[0]
# for i in lst:
#     maxi=max(maxi,i)
# secondmax=lst[0]
# for i in lst:
#     if i>secondmax and i < maxi:
#         secondmax=i
#
# print(secondmax)

#Find same in one iteration
large=float('-inf')
secondlarge=float('-inf')
for i in range(len(lst)):
    if lst[i]> large:
        secondlarge=large
        large=lst[i]
    elif lst[i]>secondlarge and   lst[i]!=large:
        secondlarge=lst[i]

print(secondlarge,large)