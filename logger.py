import datetime

def save_log(question, answer):
    with open("logs/chat_log.txt", "a", encoding="utf-8") as file:
        file.write(f"\nTime: {datetime.datetime.now()}\n")
        file.write(f"User: {question}\n")
        file.write(f"AI: {answer}\n")
        file.write("-" * 50 + "\n")