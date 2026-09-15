from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

from langchain_core.prompts import PromptTemplate, load_prompt
# Load environment variables from .env
load_dotenv()

st.header("Research Tool")

model = ChatOpenAI(model="gpt-5.6")

# static prompt
# user_input = st.text_input("Enter your prompt")

# # if st.button("Summarize"):
# #     if user_input.strip():
# #         # result = model.invoke(user_input)
# #         ResourceWarning
# #         st.write(result.content)
# #     else:
# #         st.warning("Please enter a prompt.")


# if st.button('Summarize'):
#     st.write('hello')



# -------------------------
# User inputs
# -------------------------
# Dynamic prompt
paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)

# -------------------------
# Dynamic Prompt Template
# -------------------------

template = PromptTemplate(
    template="""
Explain the research paper "{paper_name}".

Use the following explanation style:
{style}

Use the following explanation length:
{length}

Explain the paper clearly and cover:
1. The main problem the paper is solving
2. The key idea
3. How the proposed method works
4. Important architecture or algorithm details
5. Main results
6. Why this paper is important
""",
    input_variables=[
        "paper_name",
        "style",
        "length"
    ]
)

# -------------------------
# Run when button clicked
# -------------------------

if st.button("Summarize"):

    prompt = template.invoke({
        "paper_name": paper_input,
        "style": style_input,
        "length": length_input
    })

    result = model.invoke(prompt)

    st.write(result.content)