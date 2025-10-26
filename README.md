🌍 TranslationApp
  
    A simple yet powerful Python application that translates text between languages — now with voice assistance to speak and translate in real time!

🧠 Overview

 
    TranslationApp is a simple yet powerful Python-based translation tool that allows you to translate text between languages — with built-in voice assistance for real-time speak & translate functionality.
    
    You can type or speak text, get instant translations, and even hear the output spoken aloud in your target language. Perfect for learning, travel, or accessibility use cases.

🚀 Features
  
    ✨ Text Translation – Instantly translate text between multiple languages
    🎤 Voice Input – Speak directly and let the app recognize your words
    🔊 Text-to-Speech Output – Hear the translated output spoken aloud
    🧩 Modular Design – Easy to integrate into other projects
    💡 Cross-Platform – Works on Windows, macOS, and Linux

📦 Installation
  
  1. Clone this repository and install dependencies:
  
    git clone https://github.com/arnavpathak10/TranslationApp.git
  
    cd TranslationApp
    
    pip install -r requirements.txt
  
  
  2. (Recommended) Create a virtual environment:
    
    python3 -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
  
  3. Install the dependencies:
  
    pip install -r requirements.txt

💬 Usage
  📝 Text Translation
    from languageTranslationFunction import translate_text
    
    result = translate_text(source_lang="en", target_lang="fr", text="Good morning!")
    print("Translated text:", result)

🎙️ Voice Translation
    from voiceTranslator import voice_translate
    
    voice_translate(source_lang="en", target_lang="es")
  
    
  This mode:
  
  Listens for your voice 🎧
  
  Converts speech to text 🗣️
  
  Translates it 🌐
  
  Speaks the translated output aloud 🔊

🗣️ Voice Assistance Details

  The voice assistance system combines:

🧠 SpeechRecognition – Captures and processes microphone input

  🗣️ gTTS (Google Text-to-Speech) – Converts text back to audio
  
  ⚙️ Optional custom APIs for translation
  
  This enables hands-free translation — just speak and listen to your translated message in real time!

🧾 Requirements
  
  Python 3.8 or above
  
  Internet connection (for APIs and TTS)
  
  Microphone & speakers (for voice translation)
  
  Dependencies listed in requirements.txt

📂 Project Structure
  TranslationApp/
  │
  ├── languageTranslationFunction.py    # Core translation logic
  ├── voiceTranslator.py                # Voice input + text-to-speech logic
  ├── requirements.txt                  # Dependencies
  ├── layouts/                          # (Optional UI or layout files)
  └── __pycache__/                      # Cached files

🖼️ Screenshots & Demos

  You can add these later after capturing screenshots or short GIFs.
  
  Mode	Screenshot / Demo
  
  Voice Translation	- <img width="1308" height="752" alt="image" src="https://github.com/user-attachments/assets/b8ae81fe-a533-45cc-8589-c7a73afa26ba" />
  Translated Text - <img width="1309" height="760" alt="Screenshot 2025-10-26 151852" src="https://github.com/user-attachments/assets/044db68f-1064-4a00-b3ff-8f1084d0e3fe" />


🤝 Contributing

  Contributions, bug reports, and feature requests are welcome!
  To contribute:
  
  Fork this repository
  
  Create a new branch (feature/your-feature)
  
  Commit and push your changes
  
  Open a pull request 🎉

🪪 License
  
  This project is licensed under the MIT License.


💬 Author

👨‍💻 Arnav Pathak

If you enjoy this project, consider giving it a ⭐ on GitHub — it really helps!

“Translate your thoughts effortlessly — with your voice, your words, and your world.” 🌐🎧
