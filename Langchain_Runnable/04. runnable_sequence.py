from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

load_dotenv()
model = ChatOpenAI()


prompt1 = PromptTemplate(
    template = 'write a joke about this {topic}',
    input_variable = ['topic']
)

prompt2 = PromptTemplate(
    template = 'describe the following joke - {text}',
    input_variable = ['text']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)


final_output = chain.invoke({'topic':'Machine learning'})

print(final_output)