class A():

    def dothis(self):
        print("doing this in A")


class B(A):
    pass


class C():
    def dothis(self):
        print("doing this in C")


class D(C,A):
    pass

d_instance = D()
d_instance.dothis()