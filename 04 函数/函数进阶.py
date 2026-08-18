#全局变量 局部变量

#globle关键字  全局变量，声明后能在函数里修改全局变量  通常用于程序状态，配置，计数器

#传参方式：
# 位置传参；
# 关键字传参(无顺序)stu=reg(name="张三"，age=18)
#混合：先位置后关键字

#默认参数（缺省参数）
# def reg_stu(name,age,gender="男",city="北京"):
#     print(name,age,gender,city)
#     return{"name":name,"age":age,"gender":gender,"city":city}
# stu=reg_stu("张三",18,"男","河南")
# print(stu)

#不定长参数

#1.位置参数//元组
# def calc_data(*args):
#     min_data=min(args)
#     max_data=max(args)
#     avg_data=sum(args)/len(args)
#     return min_data,max_data,round(avg_data,2)
#
# data=calc_data(12,56,42,3,25,18,88)
# print(data)

# #2.关键字参数
# def calc_data(*args,**kwargs):
#     '''
#
#     :param args: 不定常位置参数
#     :param kwargs: 不定常关键字参数
#     :return:
#     '''
#     min_data=min(args)
#     max_data=max(args)
#     avg_data=sum(args)/len(args)
#
#     if kwargs.get("round"):
#         avg_data=round(avg_data,kwargs["round"])
#     if kwargs.get("print"):
#         print(f"最大值：{max_data},最小值：{min_data},平均值：{avg_data}")
#     return min_data,max_data,round(avg_data,2)
#
# data=calc_data(12,56,42,3,25,18,88,round=2,print=True)
# print(data)

#函数参数类型：数字，布尔，字符串，元组，列表，集合，字典
#特殊：函数   return oper(x,y),要调用

#匿名函数 lambda表达式
# lambda 参数列表：函数体
# eg: lambda x,y:x+y   自动返回
# add=lambda x,y:x+y
# print(add(1,2))

#案例1
# def jiecheng(num):
#     sum=1
#     for i in range(1,num+1):
#         sum=sum*i
#     return sum
# print(jiecheng(1))
# #递归：
# def jiecheng(n):
#     if n==1:
#         return 1
#     else:
#         return n*jiecheng(n-1)
# print(jiecheng(4))

# # 案例2
# def cost(*args:tuple[str,float,int],coupon=0,score=0,express=0):
#     total_price=[goods[1]*goods[2] for goods in args]
#     total_cost=sum(total_price)
#
#     if total_cost>=5000:
#         total_cost-=coupon
#
#     if total_cost>=5000 and score//100<=total_cost:
#         total_cost-=score//100
#
#     total_cost+=express
#     return total_cost
#
# #类型注解
# a=5
# b: str="Python"
# goods: tuple[str,int,int]=("手机",9999,5)
#
# #函数-类型注解
# def calc(r:float)->tuple[float,float]:
#     return round(3.14*r*r),round(2*3.14*r)
# print(calc(10))

#导入模块
# import 模块名       ramdom.randint(10,100)
# import 模块名 as 别名
# from 模块名 import 功能名   randint(10,100)
# from 模块名 import 功能名 as 别名
# from 模块名 import*
#案例
# from random import*
# for i in range(5):
#     print(randint(10,100))

#自定义模块
#常量：名称全大写
# print("-"*30)

#__name__:当前模块的名字（python内置变量，直接运行当前模块，__name__的值为"__main__"）
#执行当前文件会执行以下代码，如果被当模块导入，则不执行
# print(__name__)
# if __name__=='__main__':
#     log_seporater()

#__all__模块级特殊变量，用于指定 from 模块名 import* 时会导入那些功能
__all__ =["log_seeporator1","log_seeporator3","PI"]

#模块package(包):包含__init__.py   包->模块->功能
import 包名.模块名.功能名
#如果要通过*导入，需要在__init__.py里增加特殊变量__all__=[]