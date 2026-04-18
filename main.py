from voice.voice_input import listen
from voice.voice_output import speak
from core.ai_engine import get_response
from logger import save_log
from core.text_normalizer import normalize_text

print("GrameenAI Assistant Started...")
print("Speak something...\n")

while True:
    try:
        text = listen()
        text = normalize_text(text)

        if not text:
            continue

        print("User:", text)

        response = get_response(text)

        print("AI:", response)

        speak(response)

        save_log(text, response)

    except KeyboardInterrupt:
        print("\nStopping GrameenAI...")
        break

    except Exception as e:
        print("Error:", e)