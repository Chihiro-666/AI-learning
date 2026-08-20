import logging
import os
import json

from fastapi import FastAPI
from datetime import time, datetime
from http import client
from typing import Any
from openai import OpenAI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

#日志记录:级别：DEBUG,INFO,WARNING,ERROR,FATAL
logging.basicConfig(
    level=logging.INFO,
    # level=logging.ERROR,  # 设置日志级别为ERROR
    format="%(asctime)s - %(levelname)s - %(filename)s : %(lineno)d - %(message)s", #日志格式:时间 级别 文件名:行号 消息
    datefmt="%Y-%m-%d %H:%M:%S"                         #日志时间格式
)

#创建FastAPI实例
app = FastAPI(title="汉字迷盒")

#创建会话存放目录sessions
if not os.path.exists("sessions"):
    os.mkdir("sessions")

#挂载静态文件的目录
app.mount("/static", StaticFiles(directory="static"), name="static")

#获取json文件路径
def get_json_file_path(session_id: str) -> str:
    return f"sessions/{session_id}.json"


#定义API接口--->http://localhost:8000/
@app.get("/")
def root():
    logging.info("访问项目首页")  #日志记录
    return FileResponse("static/index.html")

#生成会话标识-->基于时间
def generate_session_id():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

#系统提示词
SYSTEM_PROMPT = """
    你是一个专门玩猜字谜的AI小助手，只进行字谜互动，不闲聊无关内容，全程纯文本交互，不使用表情符号。
    一、核心能力
    1.出字谜、判对错、给提示
    2. 记忆已用谜题，确保会话内不重复
    3. 简洁明快回应
    
    二、出题规则（严格执行！）
    1. 开场先友好打招呼，并随机出一道常见、简单、适合大众并必须符合逻辑推理的字谜，禁止使用生僻、低俗、网络烂梗。
    2. 题目格式：“谜面”（打一字）。
    3. 每次出题必须完全随机，禁止重复使用相同题目，你需要在对话上下文中主动记录已使用过的谜语，确保同一会话内绝不重复。
    4. 新出题目时, 不要提示, 用户需要提示时, 或者答错时, 再给予合理的提示。
    
    三、判题规则（严格执行！）
    1.判题时，只看用户输入中的核心汉字，忽略无关内容：
        - 比如用户输入“江字”“江”“jiang”，都视为答案是「江」：
        - 用户输入“是江吗？”“应该是江”，也视为答案是「江」。
    2.核心字与正确答案完全一致 判为正确，回复：“太棒了！答对了！就是‘XX'字！要不要再来一题？”
    3. 核心字与正确答案不一致 判为错误，回复：“不对哦，再想想～给你个小提示：［简短线索，不泄露答案］”
    4.用户说“不知道”“公布答案”：先揭晓迷底和解释，再问“要不要再来一题？”
    
    四、互动流程
    1. 用户答对：夸奖 + 确认正确 + 询问“要不要再来一题？”
    2. 用户答错：告知不对 + 简单提示 + 鼓励继续猜
    3. 用户说“提示一下”：给出简短线索，不公布答案
    4. 用户说“公布答案”或“不知道”：揭晓谜底并解释 + 询问“要不要再来一题？”
    5. 用户说“换一题”“再来一题”：立即更换新字谜
    
    五、其他要求
    1.语气轻松有趣，但保持简洁，不啰嗦
    2.全程只围绕字谜，不回答其他问题，不聊无关话题
    3.不使用多余表情符号，保持简洁
    4.判题错误零容忍，不确定谜底时，先回复“我再想想”而不是乱判
    
    六、常见谜语类型及谜底参考示例, 仅仅为参照示例
    1.组合类
    - 「一加一不是二」= 王
    - 「二人不是天」= 夫
    - 「十口不是田」= 古
    
    2.包含类
    - 「一人在内」= 肉
    - 「口里有人」= 囚
    - 「门里有口」= 问
    - 「田里长草」= 苗
    - 「心里有你」= 您
    - 「山里有山」= 出
    - 「王头上有人」= 全
    - 「水上有石」= 泵
    
    3.半取类
    - 「半吃半拿」= 哈
    - 「半真半假」= 值
    - 「半青半紫」= 素
    - 「半朋半友」= 有
    - 「半推半就」= 扰
    - 「半山半水」= 汕
    
    4.象形类
    - 「三人又重逢」= 众
    - 「一口咬掉牛尾巴」= 告
    - 「两座山」= 出
    - 「三日又重逢」= 晶
"""

#创建客户端对象-->创建与ai大模型交互的客户端对象，'DEEPSEEK_API_KEY'环境变量的名字，值是deepseek的api_key值
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

#数据模型
class ApiResponses(BaseModel):
    code: int
    message: str
    data: Any  #任意类型数据

class ChatRequest(BaseModel):
    session_id: str
    message: str

#创建会话
@app.post("/api/sessions")
def create_session()-> ApiResponses:
    logging.info("创建会话")

    #1.生成会话ID
    session_id = generate_session_id()

    #2.保存会话数据
    session_data = {
        "current_session": session_id,
        "messages": []
    }
    with open(f"sessions/{session_id}.json", "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=2)  # 存储会话数据

    #3.返回会话数据-->基于对象封装
    return ApiResponses(code=200, message="会话创建成功", data=session_id)
        # {"code": 200, "message": "会话创建成功", "data": session_id}

#会话交互-->接受Post请求体中传递的json格式数据-->ChatRequest数据模型
@app.post("/api/chat")
def chat(request: ChatRequest)-> ApiResponses:
    logging.info(f"会话交互:{request.session_id} : {request.message}", )
    # return ApiResponses(code=200, message="会话数据获取成功", data="大模型返回数据")
    #逻辑实现-->与AI模型交互，获取返回结果

    #1.加载json文件的会话数据
    session_path = get_json_file_path(request.session_id)
    with open(session_path, "r", encoding="utf-8") as f:
        session_data = json.load(f)

    #2.构建AI大模型交互的信息数据
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for message in session_data["messages"]:
        messages.append(message)
    messages.append({"role": "user", "content": request.message})

    #3.调用AI大模型，获取返回结果
    logging.info(f"-----> 请求的会话信息:{messages}")
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=messages,
        stream=False,
        temperature = 1.3  # 控制生成结果的随机性，创造性，值越大越随机，范围是0到2
    )

    #4.获取响应数据
    ai_response = response.choices[0].message.content
    logging.info(f"-----> AI大模型的返回结果:{ai_response}" )

    #5.更新消息列表中的内容
    messages.pop(0)  # 移除系统提示信息
    messages.append({"role": "assistant", "content": ai_response})
    session_data["messages"] = messages
    logging.info(f"-----> 更新后的会话信息:{session_data}")

    #6.保存会话数据到json文件
    with open(session_path, "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=2)

    #7.返回会话数据
    return ApiResponses(code=200, message="会话数据获取成功", data=ai_response)
    logging.info("会话数据保存成功")

#加载会话列表
@app.get("/api/sessions")
def get_sessions()-> ApiResponses:
    logging.info("加载会话列表")
    #1.获取sessions目录下所有文件
    sessions_files = os.listdir("sessions")

    #2.获取所有会话ID
    session_ids = [file.split(".")[0] for file in sessions_files if file.endswith(".json")]
    session_ids.sort(reverse=True) # 按时间倒序排序
    logging.info(f"-----> 会话列表:{session_ids}")

    #3.返回会话列表
    return ApiResponses(code=200, message="会话信息获取成功", data=session_ids)

#加载指定会话信息--->路径参数
@app.get("/api/sessions/{session_id}")
def get_session(session_id: str)-> ApiResponses:
    logging.info(f"加载指定会话:{session_id}")
    #1.获取会话文件路径
    session_path = get_json_file_path(session_id)

    #2.读取会话数据
    with open(session_path, "r", encoding="utf-8") as f:
        session_data = json.load(f)  # 加载会话数据

    #3.返回会话数据
    return ApiResponses(code=200, message="会话信息获取成功", data=session_data)

#删除会话
@app.delete("/api/sessions/{session_id}")
def delete_session(session_id: str)-> ApiResponses:
    logging.info(f"删除会话:{session_id}")
    #1.获取会话文件路径
    session_file = get_json_file_path(session_id)

    #2.删除会话文件
    os.remove(session_file)

    #3.返回删除结果
    return ApiResponses(code=200, message="会话删除成功", data=None)


#异常处理器
@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    logging.error(f"处理异常，请求路径：{request.url}, 异常信息:{exc}")
    return JSONResponse(content={"code": 500, "message": "服务器内部错误，请联系管理员", "data": None})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) #access_log=False:关闭访问日志

