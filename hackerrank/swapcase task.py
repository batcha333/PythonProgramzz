#swapcase task
a=input("enter:")
for i in a:
    if i.islower():
        print(i.upper(),end="")
    elif i.isupper():
        print(i.lower(),end="")
    else:
        print(i,end="")
