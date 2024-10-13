lst=[1,2,6,5]
n=len(lst)
x=True
for i in range(1,n):
    if lst[i] < lst[i - 1]:
            x = False


print(x)
