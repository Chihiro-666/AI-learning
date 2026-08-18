#tuple可重复，有序，不可修改
# count()
# index()
# t=(12,62,42,85,12,47)
# print(type(t))
# #切片
# print(t[0:5:1])
# print(t.count(12))
# print(t.index(12))
#如果定义氮元素的元组，后边加逗号
# t=(100,)
# print(type(t))
#元组的组包Packing与解包Unpacking
#组包
# t=(5,6,7,2)
# t=5,6,7,2
# #基础解包
# a,b,c,d=t
# #扩展解包(*)
# x,*y,z=t   #x为5，y为[6,7],z为2
# s,*o=t     #s为5，y为[6,7,2]
# *w,z=t     #w为[5,6,7],z为2
#组包操作
# t1=(5,6,75,34,55,66)
# t2=(23,34,78,66,88,9)
#
# #解包操作
# #基础解包：元素数量相等
# a,b,c,d,e,f=t1
# print(a,b,c,d,e,f)
# #扩展解包
# x,y,*z,w=t1
# print(x,y,w)
# print(z)  #列表里

#案例1:交换（组包操作）
# a=10
# b=20
# a,b=b,a
# #t=b,a  a,b=t
# print(a,b)

#案例2：学生成绩
students=(
    ("s001","王林",58,65,98),
    ("s002","张三",96,86,78),
    ("s003","李四",96,86,78),
)
# for s in students:
#     sum=s[2]+s[3]+s[4]
#     avg=sum/3
#     print(f"{s[0]} {sum} {avg:.1f}")  #.1f,保留一位小数
#解包
for id,name,chinese,math,english in students:
    sum=chinese+math+english
    avg=sum/3
    print(f"{id} {sum} {avg:.1f}")  #.1f,保留一位小数
chinese_score=[s[2] for s in students]
print(chinese_score)
print(f"最低分:{min(chinese_score)}")
