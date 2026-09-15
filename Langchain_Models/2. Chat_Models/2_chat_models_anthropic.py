import langchain_anthropic import ChatAnthropic 
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model = "claude-3-3-sonnet-20241022")
result = model.invoke("what is the llm")

print(result.content)
