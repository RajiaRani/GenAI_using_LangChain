from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-5.6")


# Problem with this code it did not store the chat history
# while True:
#     user_input = input('you:')
#     if user_input == 'exit':
#         break
#     result = model.invoke(user_input)
#     print('AI :', result.content)


# Maintain the chat history
# created the list

# chat_history = []
# while True:
#     user_input = input('User: ')
#     chat_history.append(user_input)
#     if user_input == 'exit':
#         break
#     result = model.invoke(chat_history)
#     chat_history.append(result.content)
#     print('AI:', result.content)

# print(chat_history)


chat_history = [
    SystemMessage(content='You are a helpful assistant')
]

while True:
    user_input = input('User: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('AI:', result.content)

print(chat_history)

