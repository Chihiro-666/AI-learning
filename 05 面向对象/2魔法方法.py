#自动调用
# __init__ 初始化
# __str__
# __eq__ 比较是否相当=
# __lt__ <
# __le__ <=
# __gt__ >
# __gt__ >=

class Car:
    #方法
    def __init__(self,c_colar,c_name,c_price):
        self.colar=c_colar
        self.name=c_name
        self.price=c_price
        print("OK")

    def running(self):
        print(f"{self.name}正在高速行驶")

    def __str__(self):
        return f"{self.name} {self.colar} {self.price}"

    def __eq__(self,other):
        return self.colar == other.colar and self.name == other.name and self.price == other.price

    def __lt__(self,other):
        return self.price < other.price

c1=Car("red","X5",600000)
print(c1)
c2=Car("red","X5",500000)
print(c2)

print(c1==c2)
print(c1<c2)