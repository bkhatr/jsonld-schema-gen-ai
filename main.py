from chains.faq_chain import get_faq_schema_chain

if __name__ == "__main__":
    faq_input = """
    Q: What is solar energy?
    A: Solar energy is energy from the sun that is converted into thermal or electrical energy.
    """
    chain = get_faq_schema_chain()
    output = chain.invoke({"faq_content": faq_input})
    print(output)
