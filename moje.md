openai = OpenAI(base_url=os.getenv("GEMINI_BASE_URL"), api_key=os.getenv("GOOGLE_API_KEY"))

os.getenv("LLM_MODEL")

def push(message):
    print(f"Log: {message}")
    with open("twin_log.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")

gemini_client = AsyncOpenAI(base_url=os.getenv('GEMINI_BASE_URL'), api_key=os.getenv('GEMINI_API_KEY'))
gemini_model = OpenAIChatCompletionsModel(model=os.getenv('LLM_MODEL'), openai_client=gemini_client)
agent = Agent(name="Jokester", instructions="You are a joke teller", model=gemini_model)

  llm: gemini/gemini-3.5-flash-lite

<!--  -->

llm = ChatOpenAI(
    model=os.getenv("LLM_MODEL", "gemini-2.5-flash"),
    base_url=os.getenv("GEMINI_BASE_URL"),
    api_key=os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY"),
)
message = "In 1 sentence, what does it mean for an AI Agent to be autonomous"
reply = llm.invoke(message)
print(reply.content)

GoogleGenerativeAIEmbeddings