from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)


document = [
    "Today is sunday", 
    "i am studying ai",
    "day is very good and best ",
    "I love computer science and maths both",
]
result = embedding.embed_query(document)

print(str(result))
