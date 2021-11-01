n=int(input("e:"))
l1,l2=[],[]
dict={}
for i in range(n):
    a=input("e:")
    l1.append(a)
    b=float(input("e:"))
    l2.append(b)
    dict[l1[i]]=l2[i]
l2.sort()
d=list(set(l2))
new={}
c=d[1]
for j,k in dict.items():
    if(c==k):
        new.update({j:k})
print(new)