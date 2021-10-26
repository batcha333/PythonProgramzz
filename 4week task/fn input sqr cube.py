def inp():
    global a
    a=int(input("enter:"))
    sqr()
    cube()
def sqr():
    print(a**2)
def cube():
    print(a**3)
inp()