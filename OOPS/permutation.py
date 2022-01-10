from math import factorial
from math import *
a=[1,2,3,4]
n=len(a)
r=2
ways1=factorial(n)
ways2=factorial(n-r)
ways3=factorial(r)
ways=ways1//(ways2*ways3)
print(ways)    
