#网络爬虫（网络机器人）
#开始-->发送HTTP请求-->解析结果提取数据-->数据清洗-->保存数据-->结束

#robots协议:  robots.txt(君子协议)
# 通用规则：
#     user-agent：用户代理，告诉服务器，我是谁
#     Disallow:  不允许爬取的URL
#     Allow:  允许爬取的URL
#     Sitemp: 网站地图
#     Crawl-delay: 爬虫间隔时间

# 特定规则：
#     1.百度：
#         user-agent: Baiduspider
#         Disallow: /
#     2.谷歌：
#         user-agent: Googlebot
#         Disallow: /
#     3.搜狗：
#         user-agent: sogou spider
#         Disallow: /
#     4.必应：
#         user-agent: msnbot
#         Disallow: /
#     5.雅虎：
#         user-agent:

#前端网页结构：HTML+CSS+JS
# HTML: 网页结构（内容，页面原素材） 超文本：文本，图片，音频    标记语言：<标签名>
# CSS: 描述网页样式（外观）<style>
# JS: 描述网页行为（交互效果）<script>

#案例  安装requests:用于发送网络请求,获取响应数据
import requests
from lxml import html

#定义url
url = "https://www.tiobe.com/tiobe-index/"

#发送请求，获取数据
responses = requests.get(url)

#输出数据到控制台
# print(responses.text)
document = html.fromstring(responses.text)

#解析数据
#解析表头
# th_list = document.xpath("//table[@id='top20']/thead/tr/th/text()")
th_list = document.xpath("//*[@id='top20']/thead/tr/th/text()")
print(th_list)

#解析表格数据
tr_list = document.xpath("//table[@id='top20']/tbody/tr")
for tr in tr_list:
    td_list = tr.xpath("./td/text()")
    print(td_list)

