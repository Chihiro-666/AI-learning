"""
重写
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
        self.__control_fuel()

    def stop(self):
        print(f"{self.brand}{self.model}停止行驶...")

    def __control_fuel(self):
        print(f"{self.brand}{self.model}正在控制燃油...")

    #外部访问私有属性--->通过定义方法
    def get_owner(self):
        return self.__owner[0:1]+"**"

    def charge(self):
        print(f"{self.brand}{self.model}正在加油...")

#继承
class FuelCar(Car):
    def charge(self):
        #方式1：super().方法名()
        # super().charge()

        #方式2：类名.方法名()--->self必填
        Car.charge(self)
        print(f"{self.brand}{self.model}正在充电...")

class ElecCar(Car):
    pass

if __name__ == "__main__":
    c1 = FuelCar('BMW','黑色','A6','张三')
    c1.charge()