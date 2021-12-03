class Demo:
    def __init__(self,name,place):    #constructor method
        self.name =name
        self.place=place
    def display(self):
        print("method working")
p1=Demo("ocean","pondicherry")
print(p1)





class Demo:
    def __init__(self):    #constructor method
        print("constructor working")
    def display(self):
        print("method working")
p1=Demo()