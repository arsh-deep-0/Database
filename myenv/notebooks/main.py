import os 
from dotenv import load_dotenv
load_dotenv()
os.environ['OPENAI_API_KEY'] = "sk-proj-0VippXxEKAhmZRuMnLsAT3BlbkFJqmBbabkim9YRNSTdisOY"

from langchain_core.prompt import ChatPromptTemplate

template = """Based on the table schema below, write a SQL query that would answer the user's question:
{schema}

Question: {question}
SQL Query:"""
prompt = ChatPromptTemplate.from_template(template)
