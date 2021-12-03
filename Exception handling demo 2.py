import math
user=int(input("input:"))
try:
    print(b) #nameerror
    a=math.factorial(user)
    print(a)
except ValueError:
    print("factorial not allowed for neg numbers")
except NameError:
    print("name error")
else:
    print("else part")
finally:
    print("tq")