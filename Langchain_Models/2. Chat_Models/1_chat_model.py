from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = 'gpt-4', temperature=0.4, max_completion_tokens=10)

result = model.invoke("what is the Attention Mechanism in LLM?")
# print(result)
print(result.content)


