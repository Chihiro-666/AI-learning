import json

#写入
user= {
    "name": "张三",
    "age": 18,
    "sex": "男"
}
with open("resource/user.json", "w",encoding="utf-8") as f:
    #ensure_ascii：默认True, 如果为False，则输出unicode编码
    # indent:缩进, 默认为None
    json.dump(user, f,ensure_ascii=False,indent=2)

#读取
with open("resource/user.json", "r",encoding="utf-8") as f:
    user = json.load(f)
    print(user)
    print(type(user))