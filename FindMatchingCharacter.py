str1=set('REENE')
str2=set('NAINA')
result=''
for i in str1:
    for j in str2:
        if i==j:
           print(j)

# str_list = ["Hello", " World", " from", " Python"]
# result = "".join(str_list)  # Joins the list elements into one string
# print(result)  # Output: Hello World from Python
#optimized way
x=str1 & str2
print(type(x))
