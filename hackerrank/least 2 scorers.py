n=int(input("e:"))
l1,l2=[],[]
dict={}
for i in range(n):
    a=input("e:")
    l1.append(a)
    b=float(input("e:"))
    l2.append(b)
    dict[l1[i]]=l2[i]
d=list(set(l2))
f=list(sorted(d))
new={}
print(f)
c=f[1]
print(c)
for j,k in dict.items():
    if(c==k):
        new.update({j:k})
lis=list(new.keys())
lis.sort()
for i in lis:
    print(i)
