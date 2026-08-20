"""
多态：同一个方法，不同的实现
"""

class Car:
    def __init__(self, brand, color, model, owner):
        self.brand = brand
        self.color = color
        self.model = model
        self.__owner =owner

    def start(self):
        print(f"{self.__owner}{self.brand}{self.model}正在启动...")

    def run(self):
        print(f"{self.brand}{self.model}正在运行...")

    def stop(self):
        print(f"{self.brand}{self.model}停止行驶...")

    def __control_fuel(self):
        print(f"{self.brand}{self.model}正在控制燃油...")

    #外部访问私有属性--->通过定义方法
    def get_owner(self):
        return self.__owner[0:1]+"**"

    def charge(self):
        print(f"{self.brand}{self.model}正在加油...")

class FuelCar(Car):
    def charge(self):
        print(f"{self.brand}{self.model}正在加油...")

class ElecCar(Car):
    def charge(self):
        print(f"{self.brand}{self.model}正在充电...")

#补充燃料函数
def handle_change(car:Car):
    car.charge()

#测试代码
if __name__ == "__main__":
    #多态
    handle_change(FuelCar('BMW','黑色','A6','张三'))
    handle_change(ElecCar('BMW','黑色','A6','张三'))
