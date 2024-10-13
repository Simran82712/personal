#find given number is prime or not

num=int(input("Enter the number to check"))
count=0
for i in range(2,num):
    if num%i == 0:
        count=count+1
if count>=1:
    print("It's not Prime Number")
else:
    print("It's a Prime Number")