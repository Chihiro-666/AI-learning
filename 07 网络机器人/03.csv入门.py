#CSV : 逗号分隔值,纯文本文件,用于存储表格数据，可以直接用Excel打开
#操作：
#方式一：文件操作的原始方式
#写：
# with open("csv_data/01.csv","w",encoding = "utf-8" ,newline = "") as f:
#     # 写入表头
#     f.write("name,age,sex,hobby\n")
#     # 写入数据
#     f.write('小王,18,男,"football,java"\n')
#     f.write("小周,19,男,Python\n")
#     f.write("小李,20,女,C++")

#读
# with open("csv_data/01.csv","r",encoding = "utf-8") as f:
#     for line in f:
#         print(line.strip())

# 方式二：csv模块
import csv

with open("csv_data/02.csv","w",encoding = "utf-8",newline = "") as f:
    writer = csv.DictWriter(f,["name","age","sex","hobby"])
    writer.writeheader()  #写入表头
    writer.writerow({"name":"小王","age":18,"sex":"男","hobby":"football,java"})  #写入数据---字典
    writer.writerow({"name":"小周","age":19,"sex":"男","hobby":"Python"})
    writer.writerow({"name":"小李","age":20,"sex":"女","hobby":"C++"})
    writer.writerow({"name":"小夏","age":18,"sex":"女","hobby":"go"})

#读
with open("csv_data/02.csv","r",encoding = "utf-8") as f:
    reader = csv.DictReader(f)
    for line in reader:
        print(line)
