#while 循环

#1-100偶数累加和
# i=0
# sum=0
# while i<=100 :
#     if i%2==0:
#         sum+=i
#     i+=1
# else:
#     print(f"1-100之间的偶数和是{sum}")

#for循环
# sum=0
# for i in range(1,101):   #左闭右开
#     if i%2==0:
#         sum+=i
# else:
#     print(f"1-100之间的偶数和是{sum}")
# msg=input("请输入字符串：")
# for i in msg:
#     print(i)
# else:
#     print("END")
# range(end)
# range(start,end)  左闭右开
# range(start,end,step)

#//嵌套循环
# m=int(input("请输入行："))
# n=int(input("请输入列："))
# #print自带换行效果
# for i in range(m):
#     for j in range(n):
#         print("*",end="")  #默认/n
#     print()

#案例99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={i*j}",end="\t")
#     print()

#综合案例
# while True:
#     user = input("请输入用户名：")
#     passport = input("请输入密码：")
#     match user:
#         case"":
#             print("用户名或密码不能为空，请重新输入")
#             continue
#         case "admin" if passport == "666888":
#             print("登陆成功")
#             break
#         case "zhangsan" if passport == "123456":
#             print("登陆成功")
#             break
#         case "taoge" if passport == "888666":
#             print("登陆成功")
#             break
#         case _:
#             print("用户名或密码错误，请重新登陆")
#             continue

#综合案例2 猜数字
# import random
# num=random.randint(1,100)
# #print("数字是%s"%num)
# while True:
#     a=int(input("请输入猜测的数字："))
#     if a==num:
#         print("Game over")
#         break
#     elif a>num:
#         print("猜大了")
#     else:
#         print("猜小了")

