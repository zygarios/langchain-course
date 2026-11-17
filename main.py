from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
import os
import time

load_dotenv()


def main():
    print(f"Aktualnie używany jest model: {os.getenv('LLM_MODEL')}")
    information = """Elon Reeve Musk (wym. /ˈi:lɒn ˈmʌsk/; ur. 28 czerwca 1971 w Pretorii[4]) – południowoafrykański przemysłowiec, założyciel, współzałożyciel lub finansista przedsiębiorstw SpaceX, Tesla, Neuralink, X.com (część firmy PayPal), The Boring Company[5] oraz SpaceXAI. Pochodzi z Republiki Południowej Afryki, mieszka i pracuje w Stanach Zjednoczonych (posiada obywatelstwo południowoafrykańskie, kanadyjskie i amerykańskie). Dyrektor generalny i techniczny w SpaceX, dyrektor generalny i główny architekt w Tesla Inc. W styczniu 2021 został uznany najbogatszym człowiekiem świata przez magazyn „Forbes” i agencję Bloomberg﻿[w innych językach][6][7][8]. Od 28 października 2022 właściciel serwisu X (kiedyś „Twitter”). W okresie od 20 stycznia do 28 maja 2025 szef Departamentu Wydajności Rządu﻿[w innych językach] (ang. Department of Government Efficiency, DOGE) w drugim gabinecie Donalda Trumpa. Na dzień 2 listopada 2026 roku, według magazynu „Forbes”, jego majątek szacowany jest na 902,1 miliarda dolarów amerykańskich (USD)[1].
    """
    summary_template = """
    Given the inforamtion {information} about the person i want you to create:
    1. A short summary.
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatGoogleGenerativeAI(model=os.getenv("LLM_MODEL"))
    # llm = ChatOllama(model=os.getenv("LLM_MODEL"))
    chain = summary_prompt_template | llm

    start_time = time.perf_counter()

    response = chain.invoke({"information": information})

    elapsed = time.perf_counter() - start_time

    print(response.text)
    print(f"\nCzas odpowiedzi: {elapsed:.2f} s")


if __name__ == "__main__":
    main()
