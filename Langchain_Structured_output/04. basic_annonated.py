from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()
model = ChatOpenAI(model="gpt-5.6")

# define schema more accurate way
class Review(TypedDict):
    summary : Annotated[str, "A breif summary of the review"]
    sentiment:Annotated[str, "Positive, Nehative, Neutral"]
    product_name: Annotated[str, "The product name "]
    price: Annotated[int, "Product price details"]


structured_output = model.with_structured_output(Review)

result = structured_output.invoke("""
         I ordered this alovera liguid product with 60$ on discount
         This is a very good product and I love it.
          It is so good for my skin and hair and I take it daily.
                                  """)

print(result)
print(result["summary"])
print(result["product_name"])
print(result["sentiment"])
print(result["price"])