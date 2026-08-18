# s="Hello-Python"        #不可变性，有序性，可迭代性
# #s[4]=X#字符串无法修改
# for i in s:
#     print(i)
# print(s)
# print(s[6:])
# print(s[:6])
# print(s[6:2:-1])#反向截取

#方法  (不可变)
# find() 前到后，返回索引，无-1
# count() 出现次数
# upper()/lower() 大小写转换
# split()  按指定分隔符分割成序列
# strip() 去除字符串两端空白或指定字符
# replace() 将特定子串替换成新的子串
# startswith() 检查是否以指定子串开头，bool
#endswith()
# s="Hello-Python-Hello-World"
# print(s.find("o"))
# print(s.split("-"))
# print(s.lower())
# print(s.replace("-","_"))
# print(s.startswith("Hello"))
# print(s.endswith("Hello"))
#案例
#方式1
s=str(input("请输入邮箱："))
# if s.count("@")==1 and s.endswith("@qq.com")==True:
#     print("ok")
# else:
#     print("error")
#方式2-----in运算符
if s.count("@")==1 and "."in s:
    print("ok")
else:
    print("error")


