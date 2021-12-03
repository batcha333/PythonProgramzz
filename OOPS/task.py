def strupr(func):
    def inner(a,b):
        
        
        if( b == 0 ):
            return "invalid input"
        
        else:
            return a/b
    return inner
@strupr
def printstr(a,b):
    return a/b
print(printstr(6,0))