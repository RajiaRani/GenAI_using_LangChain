# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()


# llm = HuggingFaceEndpoint(
#     repo_id = "meta-llama/Llama-3.1-8B-Instruct",
#     task = "text-generation"
# )

# model = ChatHuggingFace(llm=llm)

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

prompt1 = template1.invoke({'topic':'machine learning'})
model_output = model.invoke(prompt1)

prompt2 = template2.invoke({'text': model_output.content})
result = model.invoke(prompt2)
print(result.content)