"""
1.前端：界面展示
    1.1html: 内容（结构）
    1.2css: 样式（表现）
    1.3js: 功能（交互）
2.后端：业务逻辑
    2.1flask: 框架
    2.2django: 框架
    2.3fastapi: 框架
3.数据库：数据存储
    3.1mysql: 关系型数据库
    3.2mongodb: 非关系型数据库
"""

"""
API接口：应用程序编程接口（接口名称、接口地址、接口参数、接口返回）
FastAPI:现代，快速，高性能的Web框架，基于标准的Python类型提示-->"构建API接口服务"
"""

from fastapi import FastAPI

# 创建FastAPI实例
app = FastAPI()

#定义API接口（路由）---> 函数的返回值表示API接口的返回数据，接口访问路径为根路径 "/"，接口名称为root，接口方法为GET
@app.get("/")
def root():
    return {"message": "Hello World"}

#定义API接口
@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"}
    ]

#启动方式
# 1.命令行： fastapi dev ".\08FastAPI入门.py"
# 2.命令行：uvicorn 08FastAPI入门:app --reload
# 3.代码运行
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


"""
Restful: 表述性状态转换，表示一种设计风格（约定，不是规定），基于HTTP协议，使用URL进行资源定位，使用HTTP方法进行操作，很规范
    1.资源定位：使用URL进行资源-->定位
    2.资源操作：使用HTTP方法进行资源-->操作
        GET：查询，获取资源
        POST：新增，创建资源
        PUT：修改更新资源
        DELETE：删除资源
    3.状态转换：使用状态码进行状态转换
    4.数据交互：使用JSON进行数据交互
    5.安全性：使用Token进行用户认证
    6.版本控制：使用URL进行版本控制
    7.路由控制：使用URL进行路由控制

"""
