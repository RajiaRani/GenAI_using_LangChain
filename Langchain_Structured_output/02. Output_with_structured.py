from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI(model="gpt-5.6")

#schema 
class Review(TypedDict):
    
    summary : str
    sentiment: str
    product_name: str


structured_model = model.with_structured_output(Review)

result = structured_model.invoke(
    """
    I ordered this alovera liguid product.
    This is a very good product and I love it.
    It is so good for my skin and hair and I take it daily.
    """
)
print(result)
print(result['summary'])
print(result['sentiment'])
print(result['product_name'])