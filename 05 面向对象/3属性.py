#实例属性；每个具体对象的属性，独立
# 类属性：所有实例共享
#先查找实例属性后类属性

class Car:
    #类属性
    wheel=4
    tax_rate=0.1

    def __init__(self,c_colar,c_name,c_price):
        #实例属性
        self.colar=c_colar
        self.name=c_name
        self.price=c_price
        self.wheel=2
        print("OK")

    def running(self):
        print(f"{self.name}正在高速行驶")

    def total_cost(self,discount,rate=0.1):
        return self.price*discount+self.price*rate

c1=Car("red","X5",500000)
print(c1.wheel)

#类名访问类属性
print(Car.wheel)
