#encapsulation
class A:
    a=5
    _b=10
    __c=15
    def display(self):
        print(self.a)
        print(self._b)
        print(self.__c)
o=A()
o.display()
class B(A):
    def display(self):
        print(self.__c)

class C(B):
    def display(self):
        print(self._b)
        print(self.__c)
o2=C()
o2.display()
        
