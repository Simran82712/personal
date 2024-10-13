# count how many times Simu appears in : simu is a girl simu is Engineer and a model
str = "simu is a girl simu is Engineer and a model"
lst=str.split()
result={}
for i in lst:
    if i not in result.keys() :
        result[i]=0
    result[i]=result[i]+1
print(result)
print((result.values()))



