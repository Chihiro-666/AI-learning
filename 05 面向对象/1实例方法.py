#对象：属性+方法   基于类
#类：相同属性和方法模版
# class 类名:
#     pass
#创建对象

#定义类（动态）
# 对象名=类名()  //大驼峰命名法
# 对象名.属性1=属性值1
# class Car:
#     pass
# c1=Car()
# c1.brand="BMN"
# c1.name="X5"
# c1.price=500000
# c1.color="red"
# #字典形式存储属性值
# print(c1.color)
# print(c1.__dict__)

#定义类
# class 类名：
#     def__init__(self,参数列表)  //初始化方法，自动调用（设置对象属性）
#     self.属性名=参数值
#     self.属性名=参数值
#
# class Car:
#     #方法
#     def __init__(self,c_colar,c_name,c_price):
#         self.colar=c_colar
#         self.name=c_name
#         self.price=c_price
#         print("OK")
#
#     def running(self):
#         print(f"{self.name}正在高速行驶")
#
#     def total_cost(self,discount,rate=0.1):
#         '''
#
#         :param discount:
#         :param rate:
#         :return:
#         '''
#         return self.price*discount+self.price*rate
#
# c1=Car("red","X5",500000)
# c1.running()
# total_cost=c1.total_cost(0.8,0.15)
# print(f"总价：{total_cost:.2f}")  //保留小数位数
# print(c1.__dict__)


