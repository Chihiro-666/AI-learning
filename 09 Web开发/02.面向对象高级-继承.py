"""
继承：子类继承父类的非私有的属性和方法
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

#继承
class FuelCar(Car):
    pass

class ElecCar(Car):
    pass

if __name__ == "__main__":
    c1 = FuelCar('BMW','黑色','A6','张三')
    c1.start()
    c1.run()
    c1.stop()
    print(c1.brand)
    print(c1.model)
    print(c1.color)
    print(c1.get_owner())