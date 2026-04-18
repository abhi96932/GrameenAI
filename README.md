🌾 GrameenAI – Rural AI Voice Assistant

GrameenAI is a Python-based AI assistant designed to support rural communities with voice interaction, smart advisory, and local data insights.
It focuses on making AI accessible through speech-based communication for farmers and rural users.

🚀 Key Features
🗣️ Voice-Based Interaction
Speech-to-text input
Text-to-speech output
Hands-free AI assistant experience
🤖 AI Engine
Intelligent response system
Context-based conversation
Chat logging for improvements
🌱 Farmer Advisory System
Uses farmer_advisory.json for guidance
कृषि (agriculture) related suggestions
Rural-focused knowledge base
📊 Rural Data Integration
Uses rural_data.json
Local insights and recommendations
🖥️ Desktop Application
Simple Python-based desktop interface
Lightweight and easy to run
🛠️ Tech Stack
Language: Python 🐍
Voice Processing: SpeechRecognition / PyAudio (assumed)
Text-to-Speech: pyttsx3 / gTTS
Data Storage: JSON files
Logging: Custom logger system
📂 Project Structure
GrameenAI/
│── ai_engine.py           # Core AI logic
│── main.py                # Entry point
│── desktop_app.py         # UI / Desktop interface
│── config.py              # Configuration settings
│── logger.py              # Logging system
│
│── voice_input.py         # Speech recognition
│── voice_output.py        # Text-to-speech
│── sound_utils.py         # Audio utilities
│
│── text_normalizer.py     # Text processing
│
│── farmer_advisory.json   # Agriculture knowledge
│── rural_data.json        # Rural insights data
│
│── chat_log.txt           # Conversation logs
│
│── test_voice.py          # Voice testing
│── test_speak.py          # TTS testing
│── test_basic_speak.py    # Basic speech test
│── python test_voice.py   # (typo file - can be removed)
│── python check_mic.py    # Mic testing script
│
│── requirements.txt       # Dependencies
⚙️ Installation & Setup
1. Clone Repository
git clone https://github.com/abhi96932/GrameenAI.git
cd GrameenAI
2. Install Dependencies
pip install -r requirements.txt
3. Run the Project
python main.py
🎙️ How It Works
User speaks through microphone 🎤
voice_input.py converts speech → text
ai_engine.py processes query
Data fetched from JSON / logic
Response converted to voice via voice_output.py 🔊
🔥 Future Improvements
🌐 Multi-language support (Hindi + regional languages)
📱 Mobile app version
☁️ Cloud-based AI model integration
📡 Offline mode for villages
📊 Real-time weather & mandi price API
⚠️ Known Issues
Some test files have inconsistent naming (python test_voice.py)
Requires microphone setup
Voice accuracy depends on environment
🤝 Contributing

Contributions are welcome!

Fork the repository
Create a new branch
Commit changes
Open Pull Request
📜 License

MIT License

👨‍💻 Author

Abhi
GitHub: https://github.com/abhi96932

🌟 Project Goal

"To bring AI to every village and empower farmers with smart technology."
