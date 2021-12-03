
def strupr(func):
    def inner():
        str1 = func()
        for i in str1:
            return i.upper()
    return inner

def listspli(func):
    def inner():
        str1 = func()
        return str1.split()
    return inner
@strupr
@listspli
def printstr():
    return "good morning"

print(printstr())
