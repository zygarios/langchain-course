llm = ChatGoogleGenerativeAI(model=os.getenv("LLM_MODEL"))
llm = ChatOllama(model=os.getenv("LLM_MODEL"))