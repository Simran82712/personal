# find out the pair that is equal to the given sum element
sum = 17
lst = [3, 4, 5, 7, 8, 9, 19, 11]
n = len(lst)
a=0
b=0
for i in range(n):
    for j in range(i + 1, n):
        if lst[i] + lst[j] == sum:
            a = lst[i]
            b = lst[j]
print(a, b)
