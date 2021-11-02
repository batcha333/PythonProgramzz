x=input().split(" ")
a=list(map(int,x))
a=list(set(x))
print(a[-2])
'''n = int(input(""))
l=[]
for i in range(n):
    a=int(input(""))
    l.append(a)
    l.sort()    
if(l[-1]==l[-2]):
    print(l[-3])
else:
    print(l[-2])'''