from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()


# The whole query becomes one vector. Not one per token.
# dimensions=32 means the entire input string — however long — comes back as a single list of 32 numbers.
# "today I am studying"
#         ↓  tokenize
#    [today] [I] [am] [studying]
#         ↓  transformer — each token gets its own vector, and
#            each one absorbs context from its neighbours
#    [·32·]  [·32·] [·32·] [·32·]
#         ↓  pooling  ← the step you were missing
#         [·32·]                    ONE vector for the whole text


embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=12)

result = embedding.embed_query("Hello, I am studing ai")

print(str(result))