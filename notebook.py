#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
from dotenv import load_dotenv

load_dotenv()

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# MODEL = "llama2"
MODEL = "gemma3n:e2b"


# In[3]:


from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

model = Ollama(model = MODEL)
embedding = OllamaEmbeddings()
chat = model | parser


# In[4]:


chat.invoke("tell me something funny")


# In[5]:


from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("jobspecs.pdf")
pages = loader.load_and_split()
pages


# In[6]:


from langchain.prompts import PromptTemplate

template = """
Answear the question based on the context below, if you can't answear the question
reply with 'I don't know'

Context: {context}

Question: {question}

"""

prompt = PromptTemplate.from_template(template)
prompt.format(question = "there is some question", context = "there is some context")


# In[7]:


chat = prompt | model | parser
chat.invoke({"context": "I am on England and weather is very bad", "question":"what country you currently at and how is the weather?"})


# In[8]:


chat.input_schema.schema()


# In[9]:


from langchain_community.vectorstores import DocArrayInMemorySearch

vectorstore = DocArrayInMemorySearch.from_documents(pages, embedding=embedding)


# In[10]:


retriever = vectorstore.as_retriever()

retriever.invoke("Passangers")


# In[11]:


from operator import itemgetter
chat = (
    {
        "context": itemgetter("question") | retriever , 
        "question": itemgetter("question")
    } | prompt | model | parser
)


# In[14]:


questions = [
    "what location is this job in?",
    "can this job be remotely",
    "what is the salary?",
    "what skills do we need to have?"
]

for question in questions:
    print(f"question: {question}")
    answ = chat.invoke({"question": question})
    print(f"answear: {answ}")


# In[15]:


for s in chat.stream({"question": "can this job be done entirely remotely like full-remote without going to office anytime"}):
    print(s, end="", flush=True)


# In[17]:


chat.batch([{"question": q} for q in questions])


# In[ ]:




