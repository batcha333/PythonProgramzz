class Father:
    def work1(self):
        print("Father is working")
        super().work()
class Mother:
    def work2(self):
        print("Mother is cooking")    
class Son(Father,Mother):
    gender="m"
    def Study(self):
        print("Son is studying")
class Daughter(Father,Mother):
    gender="f"
    def Study(self):
        print("Daughter is studying")
obj=Son()
print(obj.gender)
obj.work1
obj=Daughter()
print(obj.gender)
obj.work2