import pyttsx3
import command_processing
def tts(text):
    if "COMMAND" in text:
        command_processing.process(text)
        break
    engine = pyttsx3.init()
    engine.save_to_file(text,"voice.mp3")
    engine.runAndWait()