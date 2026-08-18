# 定义函数
# def 函数名（参数列表）：
#     函数体
#     。。。。
#     return 返回值  //可有可无

# 调用函数
# 函数名（参数）
#*多个返回值会封装到元组（）
#*round(_,num) 保留num位小数

#函数说明文档'''     '''
#用help函数或悬浮鼠标
# def rec(l,w):
#     '''
#     根据长宽求面积
#     :param l:
#     :param w:
#     :return:
#     '''
#     area=l*w
#     return area
# help(rec)
# print(rec(5,12))

#函数嵌套

#案例
def area(a,b):
    '''
    根据底和高求三角形面积
    :param a:
    :param b:
    :return:
    '''
    return a*b/2

def yuanyin_num(s):
    '''
    字符串中元音字母数量
    :param s:
    :return:
    '''
    num=0
    for i in s:
        if i in "aeiouAEIOU":
            num+=1
    return num
print(yuanyin_num("sjfjdsncshdusdhwijskkall;[P"))