"""
鸭子类型的多态：关注对象的行为，而不是对象的类型 ; 不依据于继承关系
"""

class Duck:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f"Duck{self.age}岁的{self.name}正在游泳...")

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def swimming(self) :
        print(f"Dog{self.age}岁的{self.name}正在游泳...")

class Pig:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f"Pig{self.age}岁的{self.name}正在游泳...")

def go_swimming(duck:Duck):  #类型注解：不是强制性的
    duck.swimming()

#测试代码
if __name__ == "__main__":
    duck = Duck("小鸭",1)
    dog = Dog("小狗",2)
    pig = Pig("小猪",3)
    go_swimming(duck)
    go_swimming(dog)
    go_swimming(pig)

