import json
import ai_response
import text_to_speech
import random


wakeup_file = "wake_up_words.txt"

context_prompt = f"You are a AI voice assistant in someones home, your task is to respond in the most accurate way possible to all questions asked. if someone asks you to do something physical for example open the bedroom windows, you will answer with COMMAND open bedroom windows (TEPLATE: COMMAND [action] [device]). Lets start: "
def detect_command(text):
    text = json.loads(text)
    text = text["text"]
    text = text.split(" ")
    with open(wakeup_file, "r") as file:
        for line in file:
            line = line.strip()
            for j in text:
                if line == j:
                    text = " ".join(text)
                    proompt = text + context_prompt
                    text_to_speech.tts(ai_response.get_answer(prompt=proompt))
                    return

