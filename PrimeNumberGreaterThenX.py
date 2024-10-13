# given a number n then return the prime numbers which are less then x
num=int(input("Enter the number to check"))
def isPrimeNumber(x):
 count=0
 if x<2:
  return False
 else:
  for i in range(2,x):
   if x%i==0:
    return False

  return True

def func(num):
 result=[]
 for i in range(2,num):
  if(isPrimeNumber(i)):
   result.append(i)
 return result

print(func(num))
