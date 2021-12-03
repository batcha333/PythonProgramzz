#generator fn
l=[1,2,3,4,5]
def fname():
    count=0
    for i in l:
        if i%2==0:
            count+=1
            return count