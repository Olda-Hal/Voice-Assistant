import pyttsx3
def tts(text):
    engine = pyttsx3.init()
    engine.save_to_file(text,"voice.mp3")
    engine.runAndWait()