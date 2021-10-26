a=[]
b=[1,2,3,4,5,6,7,8,9]
def foot():
    global a
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append('_')
def move():
    global x,o
    x=int(input("p x:"))
    o=int(input("p o:"))
def game():
    foot()
    move()
    global b
    if(x==1):
        a[0][0]='x'
        b.remove(x)
    elif(x==2):
        a[0][1]='x'
        b.remove(x)
    print(*a)
game()
