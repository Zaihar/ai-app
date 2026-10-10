from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0.3
)

def ask_llm(question):
    response = llm.invoke(question)
    return response.text


if __name__ == "__main__":
    print(ask_llm("Hi, introduce yourself briefly."))

