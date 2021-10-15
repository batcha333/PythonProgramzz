a=int(input("enter the number: "))
d=str(a)
i=a
arm=0
while(a):
    b=a%10
    arm+=b**len(d)
    a=a//10
print(arm)
if(i==arm):
    print(i,"is armstrong num")
else:
    print(i,"is not an armstrong number")
