import sys
import os
import tkinter as tk

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from voice.voice_input import listen
from voice.voice_output import speak
from core.ai_engine import get_response

def start_listening():
    text = listen()
    if not text:
        return

    chat.insert(tk.END, "User: " + text + "\n")

    response = get_response(text)
    chat.insert(tk.END, "AI: " + response + "\n\n")

    speak(response)


window = tk.Tk()
window.title("GrameenAI Assistant")
window.geometry("500x400")

chat = tk.Text(window)
chat.pack(pady=10)

button = tk.Button(window, text="🎤 Ask GrameenAI", command=start_listening)
button.pack()

window.mainloop()