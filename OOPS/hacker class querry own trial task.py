class Eventype():
    def __init__(self):
        self.initial=0
    def evenans(self):
        answer=self.initial
        self.initial+=2
        return answer
class Oddtype():
    def __init__(self):
        self.initial=1
    def oddans(self):
        answer=self.initial
        self.initial+=2
        return answer
odd=Oddtype()
even=Eventype()
        
querry=int(input("enter:"))
for i in range(querry):
    type,n=input().split()
    n=int(n)
    for i in range(n):
        if type=="even":
            print(even.evenans())
        elif type=="odd":
            print(odd.oddans())