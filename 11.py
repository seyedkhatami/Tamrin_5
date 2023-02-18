#Python program showing
#how MRO works

class A:
    def rk(self):
        print("In class A")

class B(A):
    def rk(self):
        print("In class B")

class C(A):
    def rk(self):
        print("In class C")


#classes ordering

class D(B, C):
    pass


r = D()
r.rk()

#output
"""
Output:
"In class B"
چون طبق فرمول خطی سازی
mro
بالاترین شاخه را پیدا میکند که در این کد کلاس 
B
است که جز پارامتر های کلاس 
D
نیز است و متد ان فراخوانی میشود

"""
        