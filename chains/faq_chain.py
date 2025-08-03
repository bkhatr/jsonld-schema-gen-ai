from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama

def get_faq_schema_chain():
    with open("prompts/faq_schema_prompt.txt") as f:
        prompt_template = PromptTemplate.from_template(f.read())

    llm = Ollama(model="llama3", temperature=0.3)
    return prompt_template | llm
