#Write a python program to convert two list into a dict
list1=['Name','Age','Salary']
list2=['Simran',24,100000]
result_dict=dict(zip(list1,list2))
print(result_dict)

#convert dictionary into tuple

for i in result_dict.items():
    print(i)
