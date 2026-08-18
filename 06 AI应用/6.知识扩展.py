#文件操作
#读文件
'''
路径写法：
    相对路径：从当前目录开始查找
    .:当前目录
    ..: 上一级目录----->../../

    绝对路径：从系统根目录开始查找，文件位置的完整路径（注意：\在字符串中代表的是转义字符，\n \t \\）
'''
with open("./resource/cat.jpg","r",encoding = "utf-8") as f:   #/=\\
    print(f.read())

#写文件
with open("test.txt","w",encoding = "utf-8") as f:
    f.write("hello world\n\n")

#追加内容
with open("test.txt","a",encoding = "utf-8") as f:
    f.write("hello world\n\n")
