#网页解析：从原始HTML文档中获取数据

#lxml: 解析HTML文档,Xpath语法,pip install lxml

#Xpath:一种语言，用于解析HTML文档，准确"定位"HTML元素
#/根节点
# // 任意位置选择节点
# . 当前节点下查找
# [n] 当前节点下第n个元素
# [last()] 当前节点下最后一个元素
# [@attr] 选择有该属性的元素
# [@attr='value'] 当前节点下属性为attr且值为value的节点
# * 匹配任意节点
# @* 匹配任意属性
# text() 获取文本内容

from lxml import html

with open("resources/img/仙逆人物志.html","r",encoding = "utf-8") as f:
    html_text = f.read()

    #解析html文本，将其解析成文档
    document = html.fromstring(html_text)

    #解析表头 -xpath语法
    th_list = document.xpath("//table/thead/tr/th/text()")
    print(th_list)

    #* : 匹配任意节点
    th_list = document.xpath("//table/thead/tr/*/text()")
    print(th_list)

    #@src: 匹配src属性
    #@*: 匹配任意属性
    th_list = document.xpath("//td/img/@src")
    print(th_list)

    #解析表格中的数据 -xpath语法
    td_list = document.xpath("//table/tbody/tr[1]/td/text()")   #tr[1]:指定行
    print(td_list)

    #获取最后行数据
    print(document.xpath("//tbody/tr[last()]/td/text()"))

    #p[@class]: 选择class属性为p的元素
    p_list = document.xpath("//p[@class]/text()")
    print(p_list)

    #p[@class=value]: 选择class属性为"xn"的p标签
    p_list = document.xpath("//p[@class='xn']/text()")
    print(p_list)

    #获取所有行数据
    tr_list = document.xpath("//table/tbody/tr")
    for tr in tr_list:
        td_list = tr.xpath("./td/text()")
        print(td_list)


