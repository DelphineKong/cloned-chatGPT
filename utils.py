from langchain.chains import ConversationChain
from langchain_community.llms import Tongyi
from langchain.memory import ConversationBufferMemory
import os
def get_chat_response(prompt,memory,api_key):
    # 设置 API-KEY
    os.environ["DASHSCOPE_API_KEY"] = api_key
    # 使用 Tongyi LLM
    llm = Tongyi()
    chain=ConversationChain(llm=llm,memory=memory)

    response=chain.invoke({"input":prompt})
    return response["response"]

# memory=ConversationBufferMemory(return_messages=True)
# print(get_chat_response("牛顿提出过哪些知名的定律？",memory,os.getenv("DASHSCOPE_API_KEY")))
# print(get_chat_response("我上一个问题是什么？",memory,os.getenv("DASHSCOPE_API_KEY")))

