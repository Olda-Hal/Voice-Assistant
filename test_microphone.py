#!/usr/bin/env python3

# prerequisites: as described in https://alphacephei.com/vosk/install and also python module `sounddevice` (simply run command `pip install sounddevice`)
# Example usage using Dutch (nl) recognition model: `python test_microphone.py -m nl`
# For more help run: `python test_microphone.py -h`

import queue
import sys
import sounddevice as sd
import wakeup_detection
from vosk import Model, KaldiRecognizer

q = queue.Queue()



def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def voice(model="en-us"):

    device = None
    device_info = sd.query_devices(device=device,kind="input")
    samplerate = int(device_info["default_samplerate"])
        
    model = Model(lang=model)
    with sd.RawInputStream(samplerate=samplerate, blocksize = 8000, device=device, dtype="int16", channels=1, callback=callback):
        rec = KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                wakeup_detection.detect_command(rec.FinalResult())
                