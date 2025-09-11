# rag-basic-system-study

This is just a basic RAG flow for data interrogation using:

- Langchain (for handling the logic flow)
- Ollama (for local inference)
- Gemma3n:e4b (the model infered locally)
- docarray and pypdf (for inmemory vector store)


```bash
$ python3 -m venv .venv
$ source .venv/bin/activate 
$ pip install -r requirements.txt
$ jupyter nbconvert --to script notebook.ipynb
$ python3 notebook.py
```
```bash
question: what location is this job in?
answear: London Area, United Kingdom.
question: can this job be remotely
answear: Yes, the job can be remotely. The job posting for Lead Backend Engineer explicitly states "London Area, United Kingdom·3 weeks ago·Over 100 applicants" and "London Area, United Kingdom(Remote)" for the Back End Developer position. The Lead Backend Engineer position also lists "London Area, United Kingdom·3 weeks ago·Over 100 applicants" and "London Area, United Kingdom(Remote)".




question: what is the salary?
answear: £90,000 - £110,000
question: what skills do we need to have?
answear: Python, FastAPI, AWS, Typescript, PostgreSQL, NumPy, Pandas.
The job posting mentions "London Area, United Kingdom (Remote)" and "Hybrid work setup—London office (King’s Cross) 1 day a week". This suggests that while there's an option to work from the London office one day a week, the role is primarily remote. 

Therefore, the answer is **Yes**. 
```

