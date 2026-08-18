# #一次性存储多个元素,      有序，可重复，可存储不同类型元素，可修改
# #也称为序列
# #eg:s=[15,56,89,76,4,6,12]
# #下标   0  1  2  3  4 5 6
# #反向索引-7-6 -5 -4 -3 -2-1
# #定义
# s=[56,35,42,"A","Hello",True]
# print(type(s))
#
# #访问
# print(s)
# #获取
# print(s[0])
# print(s[-6])
#
# #修改
# s[0]="abc"
# print(s[0])
#
# #删除
# del s[3]
# print(s)
#
# #遍历
# for i in s:
#     print(i)

#切片：[开始索引：结束索引：步长] 左闭右开/正向或反向都可/步长默认1
#eg:s[0,5,1]
# s=["A","B","C","D","E",12,56]
# print(s[0:6:2])
# print(s[:-3])  #第一个冒号不能省略
# print(type(s))

#*方法
#append()尾部追加 insert()索引之前插入 remove()删除第一个匹配值 pop()指定索引删除 sort()排序（类型一致） reverse()翻转
# s=[12,56,89,5,4,62,32,14,56]
# s.append(88)
# print(s)
# s.insert(2,50)
# print(s)
# s.remove(56)
# print(s)
# e=s.pop(3)
# print(e)
# print(s)
# s.sort()
# print(s)
# s.reverse()
# print(s)

#案例
# s=[]
# for i in range(10):
#     num=int(input("请输入数字："))
#     s.append(num)
# print(s)
# s.sort()
# print(s)
# print(s[0])
# print(s[-1])
# #sum() 求和   len()元素个数   min()最小值    max()最大值
# print("平均值：",sum(s)/len(s))

#案例2
# list1=[12,5,56,7,89,41,2,32,65,12]
# list2=[15,86,49,32,22,18,45,36]
# #合并列表
# # for num in list2:
# #     list1.append(num)
# list=list1+list2
# print(list)
# #解包
# list=[*list1,*list2]
# #组包
#
# print(list)
# #去重复记录
# for num in list1:
#     if num not in list:    #******
#         list.append(num)
# print(list)

#案例3
# list=[]
# for num in range(1,21):
#     list.append(num*num)
list=[i**2 for i in range(1,21)]  #****
print(list)
num_list=[12,56,13,22,11,45,65,88,120]
list=[i**2 for i in num_list if i%2==0]   #******
print(list)

