from langchain_ollama import ChatOllama
llm = ChatOllama(model="qwen3.5:0.8b")

def ask_llm(question):
    response = llm.invoke(question)
    return response.content
