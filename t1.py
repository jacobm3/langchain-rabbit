#!/usr/bin/python3

import os
from dotenv import load_dotenv,find_dotenv
from langchain.llms import OpenAI


load_dotenv(find_dotenv())

print(os.getenv('OPENAI_API_KEY'))

llm = OpenAI(model_name='text-davinci-003',openai_api_key=os.getenv('OPENAI_API_KEY'))

print(llm)
r = llm('explain large language models in one sentence.')
print(r)