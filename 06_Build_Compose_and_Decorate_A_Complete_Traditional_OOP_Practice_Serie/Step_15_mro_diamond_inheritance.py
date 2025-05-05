class A:
    def show(self):
        print("Show method in class A")

class B(A):
    def show(self):
        print("Show method in class B")

class C(A):
    def show(self):
        print("Show method in class C")

class D(B, C):
    pass  # D inherits from both B and C

# Example usage
obj = D()
obj.show()

# To see the MRO
print(D.__mro__)
