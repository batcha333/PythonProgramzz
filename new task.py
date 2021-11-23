from functools import reduce
a=[456,6780,985,23,45,607]
b=[]

print(b)
sum=reduce(lambda a,b:a+b,a)
product=reduce(lambda a,b:a*b,d)
if a%sum==0 and a%product==0:
    print(1)
else:
    print(0)
