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


my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

try:
    print(sum(my_list))

except Exception:
    print('There are strings in your list')