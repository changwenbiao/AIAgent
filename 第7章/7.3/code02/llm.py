import os

from langchain_openai import ChatOpenAI

def                                                                                                                                                                                                                                                                                                                                                                                                                     DeepSeek():
    # return ChatOpenAI(
    #     model= "deepseek-chat",
    #     api_key='sk-e8fadf494e074e22bef0ea26c55d3201',
    #     base_url="https://api.deepseek.com",
    # )

    return ChatOpenAI(
        model= "GLM-5.3-Flash",
        api_key='402a0784196b4b8e9af6cf2836870942.r8gHVxrQQEPr5aXE',
        base_url="https://open.bigmodel.cn/api/paas/v4",
    )