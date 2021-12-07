class Demo:
    def display(self,a=None,b=None,c=None):
        self.a=a
        self.b=b
        self.c=c
        if(a!=None and b!=None and c!=None):
            result=self.a+self.b+self.c
        elif(a!=None and b!=None):
            result=self.a+self.b
        else:
            result=self.a
        return result
o=Demo()
print(o.display(123))
def sum(a=0,b=0,c=0):
    return a+b+c
print(sum(1,2,3))