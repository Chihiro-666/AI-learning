"""
封装：将数据（属性）和操作数据的方法绑定在一起，形成一个独立的单元（类）
    1. 私有化属性：在属性名前加__
    2. 私有化方法：在方法名前加__
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

if __name__ == "__main__":
    my_car = Car("奔驰", "红色", "A6", "张三")

    # print(my_car.__owner)
    print(my_car.brand)
    print(my_car.color)
    print(my_car.model)

    my_car.start()
    my_car.run()
    my_car.stop()
    print(my_car.get_owner())
    # my_car.__control_fuel()

    #强制调用私有属性和方法：_Car
    print(my_car._Car__owner)
    my_car._Car__control_fuel()
