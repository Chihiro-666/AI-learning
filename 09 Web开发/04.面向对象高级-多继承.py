"""
多继承：一个类继承多个父类，通过逗号分隔;优先继承第一个父类
"""
from platform import version


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

#华为智驾
class HuaweiDriving:
    #华为AI智能驾驶
    def __init__(self, version):
        self.version = version

    def run(self):
        print(f"华为AI智能驾驶{self.version}正在行驶...")

#问界汽车
class WenjieCar(Car, HuaweiDriving):
    def __init__(self, brand, color, model, owner,version = "1.0"):

        # Car.__init__(self,brand, color, model, owner)
        super().__init__(brand, color, model, owner)

        HuaweiDriving.__init__(self,version)

    #重写后的run方法
    def run(self):
        Car.run(self)
        HuaweiDriving.run(self)

#
if __name__ == "__main__":
    my_car = WenjieCar("华为", "黑色", "Model 3", "张三")
    # print(my_car.__dict__)
    # print(WenjieCar.__mro__)

    my_car.run()


