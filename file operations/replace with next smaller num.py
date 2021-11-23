l=[10,9,5,4,5,3,2,1]
l1=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l1.append(l[j])
            break
    else:
        l1.append(-1)
print(l1)