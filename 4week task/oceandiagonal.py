n="ocean"
l=[3,1,0,1,3]
for i in range(5):
    for j in range(5):
        if(i==j or i+j==4):
            print(n[i],' '*l[i],end="")
    print()

            

            








'''for i in range(5):
    print(i*' ',n[i],' '*(i+l),n[i])
    l-=2
        '''