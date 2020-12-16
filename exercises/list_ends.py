import random

a = [5, 10, 15, 20, 25,6, 1, 115, 200, 205]

new_list = []

class A:

    def index_numb(self):
        for x in a:
            if x == a[0]:
                new_list.append(x)
            if x == a[-1]:
                new_list.append(x)
        print(new_list)



class B(A):
    def list_ends(self):
        return [a[0], a[len(a)-1]]



a1 = A()
b1 = B()


b1.index_numb()
b1.list_ends()