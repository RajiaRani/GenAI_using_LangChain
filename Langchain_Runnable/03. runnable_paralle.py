from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()
model = ChatOpenAI()

prompt1 = PromptTemplate(
    template = ' write about this topic {topic}',
    input_variable = ['topic']
)

prompt2 = PromptTemplate(
    template = 'write the summary for this {topic}',
    input_variable = ['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        'tweet': RunnableSequence(prompt1, model, parser),
        'linkdin': RunnableSequence(prompt2, model, parser)
    }
)

result = parallel_chain.invoke({'topic':'AI'})
# print(result)
print(result['tweet'])
print(result['linkdin'])