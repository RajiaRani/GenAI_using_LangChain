from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# define the OpenAI model name which you want to use
llm = OpenAI(model = 'gpt-3.5-turbo-instruct')

# invoke is very important method
result = llm.invoke("what is the llm")
print(result)

