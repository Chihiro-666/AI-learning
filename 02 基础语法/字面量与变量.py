# 字面量写法
# print(100)
# print(True)
# print("Hello World")
# print(None)
# print(True+1)
# base=10
# i=5
# base,i=10,5
# print("未来一个月播放总量:",base+i)
# print("未来二个月播放总量:",base+i*2)
# i="python"
# j="WWL"
# k=5
# print(i+"学会"+j+str(k))
# print("%s+%s"%(i,j))
# print(f"{i+j}")
# name=input("输入姓名：")  #一定是字符串
# age=input("输入年龄：")
# print("姓名：%s，年龄：%s"%(name,age))
# print(f"姓名：{name}，年龄：{age}")

#银行卡atm取款
# sum=1000
# password="123456"
# mima=input("输入密码：")
# money=input("输入金额：")
# if(mima!=password):
#     print("密码错误")
#     exit
# sum=sum-int(money)   #类型转换int()
# print(f"余额：{sum}")

#+-*/   //整除   %   **幂指数
# sum=10**4   #10000
# print("10**4=",sum)
# x=input("x的值：")
# y=input("y的值：")
# x=int(x)
# y=int(y)
# print("x+y=",x+y)
# print(f"x-y={x-y}")
#0.0999999999999998-->精度损失（浮点数）二进制无法表示所有小数

#21:逻辑运算符 and or not
# n=int(input("请输入一个整数："))
# print(f"{n}在10-20之间：",n>=10 and n<=20)
# n=int(input("请输入一个整数："))
# print(f"{n}不在10-20之间：",n<=10 or n>=20)

#22：if语句  if a>b:
# year=int(input("输入年份："))
# if (year%100!=0 and year%4==0)or(year%100==0 and year%400==0):
#     print("True")
# else:
#     print("False")
#25 if elif else
# grade=int(input("请输入分数："))
# if grade>=85:
#     print("优秀")
# elif grade>=60 and grade<85:
#     print("及格")
# else:
#     print("不及格")

#26 三角形案例
# a=int(input("输入a："))
# b=int(input("输入b："))
# c=int(input("输入c："))
# if a==b and b==c:
#     print("等边三角形")
# elif (a==b and a+b>c)or(b==c and b+c>a)or(c==a and c+a>b):
#     print("等腰三角形")
# elif a+b<=c or b+c<=a or c+a<=b:
#     print("不是三角形")
# else:
#     print("普通三角形")

#27 match...case 结构模式匹配
num1=float(input("请输入第一个数："))
num2=float(input("请输入第二个数："))
oper=input("请输入运算符+-*/：")
match oper:
    case "+":
        print(f"{num1}+{num2}={num1+num2}")
    case "-":
        print(f"{num1}-{num2}={num1 - num2}")
    case "*":
        print(f"{num1}*{num2}={num1 * num2}")
    case "/" if num2!=0:                           #添加条件判断
        print(f"{num1}/{num2}={num1 / num2}")
    case _:                                         # _匹配其他情况
        print("error")



