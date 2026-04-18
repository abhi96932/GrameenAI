import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer

q = queue.Queue()

model = Model("models/vosk-model-hi-0.22")
recognizer = KaldiRecognizer(model, 16000)


def callback(indata, frames, time, status):
    print("Audio received...")
    q.put(bytes(indata))


def listen():
    DEVICE_INDEX = 1

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=4000,
        dtype='int16',
        channels=1,
        device=DEVICE_INDEX,
        callback=callback
    ):
        print("🎤 बोलिए...")

        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "")

                recognizer.Reset()

                return text