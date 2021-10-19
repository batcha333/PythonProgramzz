n=int(input("enter: "))
l=[]
temp=0
for i in range(n):
    a=int(input(""))
    l.append(a)
print(l)
for i in range (n):
    for j in range(i + 1, n):
        if(l[i] > l[j]):
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
print(l[-1])
print(l[0])

     