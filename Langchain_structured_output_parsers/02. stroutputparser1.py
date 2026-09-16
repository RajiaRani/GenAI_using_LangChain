from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()


model = ChatOpenAI(model="gpt-5.6")

# Prompt 1
template1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables = ['topic']
)

# Prompt 2
template2 = PromptTemplate(
    template='write a 5 line summary on the following text./n {text}',
    input_variables = ['text']
)

# creating parser
parser = StrOutputParser()

# chain
chain = template1 | model | parser | template2 | model | parser
final_result = chain.invoke({'topic':'machine learning'})
print(final_result)

