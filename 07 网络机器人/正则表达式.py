# 正则表达式
# eg:手机号匹配 ： 1[3-9]\d{9}
# . 匹配任意字符，除了换行符
# \d 匹配数字0-9
# \D 匹配非数字0-9
# \w 匹配数字、字母、下划线
# \W 匹配非数字、字母、下划线

# \s 匹配空白字符
# [aeiou] 匹配aeiou
# [^aeiou] 匹配非aeiou
# [0-5] 匹配0-5
# [a-zA-Z] 匹配字母
# * 出现任意次（匹配0次或者多次）
# + 匹配1次或者多次（至少出现一次）
# ? 匹配0次或者1次（至多出现一次）
# {n} 匹配出现n次
# {n,} 匹配至少出现n次
# {n,m} 匹配至少出现n次，至多出现m次
# | 匹配或，左右任意一个表达式
# () 匹配括号内的表达式,将括号内的表达式作为整体匹配
# ^ 匹配字符串的开头
# $ 匹配字符串的结尾
import re

s1 = "我的手机号是15865479956你记住了吗？我的另一个手机号是15268743324，QQ号是3241266875你记住了吗？"
s2 = "15865479956是我的手机号你记住了吗？15268743324是我的另一个手机号，QQ号是3241266875你记住了吗？"

result = re.match(r"1[3-9]\d{9}",s2)   # 从开头开始匹配（返回match）
print(result) #<re.Match object; span=(0, 11), match='15865479956'>
print(result.group()) #匹配到的内容
print(result.span()) #匹配到的位置
print(result.start()) #匹配到位置的开始位置
print(result.end()) #匹配到位置的结束位置
print(result.re) #正则表达式

result = re.search(r"1[3-9]\d{9}",s1)   # 从任意位置，搜索第一个匹配项（返回match）
print(result.group())    #None没有.group,匹配不到会报错
print(result.span()) #匹配到的位置
print(result.start()) #匹配到位置的开始位置
print(result.end()) #匹配到位置的结束位置
print(result.re) #正则表达式

result = re.findall(r"1[3-9]\d{9}",s1,re.ASCII)   # 从任意位置开始，搜索所有匹配项（返回list）
print(result)