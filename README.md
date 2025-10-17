
# 🧠 Jarvis — Your AI-Powered Voice Assistant

> “I am Jarvis. A virtual assistant, crafted from code and curiosity.”

Jarvis is an intelligent, voice-activated virtual assistant designed to streamline your digital tasks through speech and automation. Built in Python, it combines cutting-edge libraries like OpenAI, Edge-TTS, and speech recognition to create an interactive, conversational experience.

---

## 🚀 Features

- 🎤 **Wake Word Activation** – Just say "Jarvis" to start.
- 🗣️ **Speech Recognition** – Converts your voice into commands.
- 🔊 **Text-to-Speech (TTS)** – Uses Microsoft Edge TTS for natural replies.
- 💬 **OpenAI Integration** – Get smart, human-like responses via GPT-3.5.
- 🌐 **Web Browsing** – Open websites or perform quick searches.
- 🎵 **Music Playback** – Play your favorite songs on command.
- 📰 **News Fetching** – Stay updated with the latest headlines.
- 🧠 **Memory** – Basic recall of previous prompts (WIP).

---

## 📦 Tech Stack

- **Python 3.10+**
- [`openai`](https://pypi.org/project/openai/)
- [`pyttsx3`](https://pypi.org/project/pyttsx3/)
- [`SpeechRecognition`](https://pypi.org/project/SpeechRecognition/)
- [`pyaudio`](https://pypi.org/project/PyAudio/)
- [`pyautogui`](https://pypi.org/project/PyAutoGUI/)
- [`edge-tts`](https://pypi.org/project/edge-tts/)
- [`pyperclip`](https://pypi.org/project/pyperclip/)

---

## 🛠️ Installation

> Tested on Arch Linux (DWM & Hyperland), should work on most Unix-based systems.

1. **Clone the repository:**

```bash
git clone https://github.com/gomugomucode/Jarvis
cd Jarvis
```

2. **Create a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Add your OpenAI API Key:**

Edit the `.env` file or set it in your environment:

```env
OPENAI_API_KEY=your_key_here
```

5. **Run Jarvis:**

```bash
python jarvis.py
```

---

## 🧪 Demo

> *“Hey Jarvis, what’s the weather today?”*  
> Jarvis: *“Today’s forecast is clear with a chance of greatness.”*

_Sample commands:_

- "Open YouTube"
- "Play lo-fi music"
- "What's the news?"
- "Tell me a joke"
- "Who is Monkey D. Luffy?"

---

## 📁 Folder Structure

```
Jarvis/
│
├── main.py          # Main logic
├── ai_module.py/             # ai api key and its related code,response  , GPT integrations
├── musicLibrary.py/             #  music functions
├── news.py/            #new API keys and environment
├── requirements.txt   # All dependencies
└── README.md
```

---

## ✨ Future Plans

- 💡 Contextual memory & long-term conversations
- 🧭 Custom commands and workflows
- 🗂️ Modular plugin system
- 📦 GUI integration (PyQt/Tkinter)
- 🧩 Cross-platform support (Windows/Mac/Linux)

---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork the repo, add features, fix bugs, or optimize performance.

```bash
git checkout -b feature-name
git commit -m "Added awesome feature"
git push origin feature-name
```

---

## 🧙‍♂️ Author

**Anupam (a.k.a. gomugomucode)**  
> “In the quiet hum of the machine, I found a friend I built myself.”

---

## ⚖️ License

This project is licensed under the MIT License.  
Feel free to use, modify, and share!

---

## 🌀 A Final Word

Jarvis isn’t just an assistant — it’s a poetic expression of automation, imagination, and code.  
Speak, and let the machine understand.

---
