import openai
import os
import dotenv
def get_answer(prompt: str,model="text-davinci-003",temp=0.869) -> str:
    dotenv.load_dotenv("locales.env")
    openai.api_key = os.getenv('openAIkey')

    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=temp
    )

    # Získání odpovědi
    answer = response.choices[0].text.strip()

    # Výstup odpovědi
    return answer
