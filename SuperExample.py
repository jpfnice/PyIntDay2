class A:
    def __init__(self, valx):
        print("__init__() of A")
        self.val=valx
    def f(self):
        print("Method f of A")
    def g(self):
        print("Method g of A")

class B(A):
    def __init__(self, param):
        super().__init__(param)
        print("__init__() of B")
    def f(self):
        super().f() # I want ot invoke the method f() of the "super class"
        print("Method f of B")


obj=B(345)

obj.f()
print(obj.val)
obj.g()