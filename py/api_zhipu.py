from zhipuai import ZhipuAI
# from enum import Enum

from config import config

class NlpModal():
    GLM4= "glm-4"
    GLM3= "glm-3-turbo"
    # ChatGlm = "chatglm_turbo"


def createClient():
    return ZhipuAI(api_key=config["zhipuai_key"])

class Message():
    def __init__(self):
        self.msgs = []

    def addMessage(self, role, content):
        self.msgs.append(
            {"role": role, "content": content}
        )
        return self
    
    def addSystemMessage(self, content):
        role = "system"
        self.addMessage(role, content)
        return self

    def addUserMessage(self, content):
        role = "user"
        self.addMessage(role, content)
        return self

    def addAssistantMessage(self, content):
        role = "assistant"
        self.addMessage(role, content)
        return self

def invokeAsyncAnswer(msgs):
    client = createClient()
    response = client.chat.completions.create(
        model= NlpModal.ChatGlm,
        messages=msgs,
        stream=True,
    )
    for chunk in response:
        print(chunk.choices[0].delta.content)


def invokeZhipu(msgs):
    client = createClient()
    res = client.chat.completions.create(
        model=NlpModal.GLM3,
        messages= msgs
    )
    return res.choices[0].message.content


if __name__ == '__main__':
    msgs = Message() \
        .addSystemMessage("请以'r:x'的格式回答我的问题，其中r是固定格式，x是问题的答案") \
        .addUserMessage("请回答521*203等于几").msgs
    res = invokeZhipu(msgs)
    print(res)

