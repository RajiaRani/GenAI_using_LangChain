# LangChain Practice

Hands-on code written while following the **Generative AI using LangChain** playlist by CampusX.

Playlist: https://www.youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0

Each folder is a self-contained topic with its own virtual environment. The scripts are
small and intentionally simple - one concept per file, run directly from the terminal.

---

## Repository layout

```
LangChain/
├── Langchain_Models/                  Working with LLMs, chat models and embeddings
│   ├── 1. LLMs/
│   ├── 2. Chat_Models/
│   ├── 3. Embedded_Models/
│   └── requirements.txt
│
├── Langchain_Prompts/                 Messages, chat history and prompt templates
│
└── Langchain_Structured_output/       Getting typed, predictable output from a model
```

---

## Requirements

- Python 3.10 or newer (these folders were created with Python 3.14)
- API keys for whichever provider you want to run:
  - OpenAI
  - Anthropic
  - Google Gemini
  - Hugging Face

Only the provider used by a given script needs a key. You do not need all four.

---

## Setup

Each topic folder has its own `venv`. Create and activate one per folder:

```bash
cd Langchain_Models
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

`Langchain_Models/requirements.txt` covers every package used across all three folders,
so the same file can be reused for the other two.

Extra package for the Streamlit app in `Langchain_Prompts`:

```bash
pip install streamlit
```

---

## Environment variables

Each folder has a `.env.example` showing which keys it expects. Copy it and fill in
your own values:

```bash
cd Langchain_Models
cp .env.example .env
```

Then edit `.env`:

```
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

Every script calls `load_dotenv()`, which reads the `.env` file from the current working
directory. Run the scripts from inside their own folder so the keys are picked up.

`.env` and `venv/` are both listed in `.gitignore`, so the real keys stay off GitHub.
`.env.example` is committed on purpose - it holds names only, never values.

---

## Running the code

```bash
cd Langchain_Models
source venv/bin/activate
python "1. LLMs/1_llm_demo.py"
```

The Streamlit app is started differently:

```bash
cd Langchain_Prompts
source venv/bin/activate
streamlit run prompt_ui.py
```

---

## What each folder covers

### Langchain_Models

| File | What it shows |
|---|---|
| `1. LLMs/1_llm_demo.py` | The plain `OpenAI` LLM wrapper and the `invoke()` method |
| `2. Chat_Models/1_chat_model.py` | `ChatOpenAI` with `temperature` and token limits |
| `2. Chat_Models/2_chat_models_anthropic.py` | Same idea using Claude through `ChatAnthropic` |
| `2. Chat_Models/3_chatmodel_google.py` | Gemini through `ChatGoogleGenerativeAI` |
| `2. Chat_Models/4_chatmodel_hf_api.py` | Hugging Face models over the hosted Inference API |
| `2. Chat_Models/5_chatmodel_huggingface.py` | Running a small Hugging Face model locally with `HuggingFacePipeline` |
| `3. Embedded_Models/1_embedding_openai_query.py` | Turning one sentence into a single vector |
| `3. Embedded_Models/02_emd_openai_multiple_queries.py` | Embedding a list of documents |
| `3. Embedded_Models/03_opensource_model.py` | Local embeddings with `all-MiniLM-L6-v2`, no API key needed |
| `3. Embedded_Models/04_document_similarity.py` | Cosine similarity search over five documents |

The first embedding file has a comment block explaining why a whole sentence comes back as
one vector instead of one vector per token - the pooling step is what collapses them.

`04_document_similarity.py` is the most complete example here: it embeds the documents and
the query, scores them with `cosine_similarity` from scikit-learn, and prints the best match.
This is the core idea behind retrieval.

### Langchain_Prompts

| File | What it shows |
|---|---|
| `01. chatbot.py` | A terminal chatbot that keeps its history using `SystemMessage`, `HumanMessage` and `AIMessage` |
| `02. messages.py` | The three message types on their own, without the loop |
| `prompt_ui.py` | A Streamlit research-paper summariser built on `PromptTemplate` |

`01. chatbot.py` keeps the earlier, broken attempts as comments above the working version.
They are worth reading in order: no history at all, then history as plain strings, then
proper message objects. The last one is the only version that lets the model tell your turns
apart from its own.

`prompt_ui.py` builds the prompt from three dropdowns - paper, explanation style and length -
and fills them into a `PromptTemplate` before sending it to the model. Type `exit` to leave
the terminal chatbot.

### Langchain_Structured_output

| File | What it shows |
|---|---|
| `01. TypedDict.py` | Plain `TypedDict`, no LangChain involved |
| `02. Output_with_structured.py` | `with_structured_output()` returning a dictionary that matches the schema |
| `03. annotated.py` | A richer schema using `Annotated`, `Optional` and `Literal` |
| `04. basic_annonated.py` | `Annotated` descriptions on each field, including a numeric one |

The point of these files is that `Annotated[str, "A brief summary of the review"]` is not
a comment. The description is sent to the model as part of the schema, so it changes what
you get back. `Literal["pos", "neg"]` restricts the answer to those two values instead of
hoping the model stays consistent.

---

## Known issues in the current code

These are left as-is because they are part of the learning process, but they will fail if
you run them without fixing them first:

- `2. Chat_Models/2_chat_models_anthropic.py` - line 1 reads `import langchain_anthropic import ChatAnthropic`; it should be `from langchain_anthropic import ChatAnthropic`. The model id `claude-3-3-sonnet-20241022` also needs to be a real Claude model id.
- `2. Chat_Models/3_chatmodel_google.py` - calls `model.inoke(...)` instead of `model.invoke(...)`.
- `3. Embedded_Models/02_emd_openai_multiple_queries.py` - passes a list to `embed_query()`. Use `embed_documents()` for a list of texts.
- `01. TypedDict.py` - uses `name = str` instead of `name: str`. With `=` these are class attributes, not type annotations, so the `TypedDict` has no fields.
- Several files in `Langchain_Prompts` and `Langchain_Structured_output` use the model id `gpt-5.6`. Change it to a model your API key actually has access to.

---

## Notes

- Hugging Face examples that run locally (`5_chatmodel_huggingface.py`, `03_opensource_model.py`) download model weights on first run, so the first execution is slow and needs disk space.
- `dimensions` on `OpenAIEmbeddings` controls the vector size. Smaller is cheaper and faster; larger keeps more detail. The examples use anywhere from 12 to 300 to make the trade-off visible.
- `tempCodeRunnerFile.py` is a leftover from the VS Code Code Runner extension and can be deleted.

