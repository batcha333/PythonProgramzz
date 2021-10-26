dic={'a':"hello",'b':'1','c':'jayalatha','d':[1,2]}
x=dic.values()
d=list(x)
new={}
d.sort(key=len)
print(d)
for i in d:       
    for k,j in dic.items():
        if(i==j):
            new.update({k:i})
print(new)











'''a,b,c=[],[],[]
for i in x:
    a.append(len(i))
    a.sort()
for i in x:
    for j in a:
        if(len(i)!=j):
            b.append(i)
        else:
            c.append(i)
print(a)
print(b)
print(c)'''

'''for i in range(len(x)):
    for j in range(1,len(x)):
        print(x[i])
        if(len(x[i])>len(x[j])):
            temp=x[i]
            x[i]=x[j]
            x[j]=temp
print(x)   
print(b)'''