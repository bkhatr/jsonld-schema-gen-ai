from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

def get_faq_schema_chain():
    with open("prompts/faq_schema_prompt.txt") as f:
        prompt_template = PromptTemplate.from_template(f.read())

    llm = OpenAI(temperature=0.3)
    return prompt_template | llm
