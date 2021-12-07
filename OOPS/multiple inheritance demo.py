class Father:
    def work(self):
        print("Father is working")
        super().work()
class Mother:
    def work(self):
        print("Mother is cooking")    
class Son(Father,Mother):
    def Study(self):
        print("Son is studying")
obj=Son()
obj.work()