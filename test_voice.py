from voice_input import listen

while True:
    text = listen()
    print("आपने कहा:", text)