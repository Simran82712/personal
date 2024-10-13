def func(s,t):
    dict1={}

    if len(s)!=len(t):
        return False

    for i in range(len(s)):
        count = 0
        if i in dict1.keys():
            count = count + 1
        else:
            count = 1
        dict1[i] = count
    for i in range(len(t)):
        if i in dict1.keys():
            dict1[i] = dict1[i] - 1
        else:
            return False

    for i in dict1.keys():
        if dict1[i] != 0:
            return False
    return True


s = "night"
t = "thing"
print(func(s,t))