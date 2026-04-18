# 🤖 AI Assistant 

A modern, web-based AI assistant that provides a seamless conversational experience using **Google Gemini**. This application is optimized for both text and voice interactions, featuring full support for the Arabic language.

## 🚀 Overview
Built with the **Streamlit** framework, this assistant is designed for accessibility and speed. Users can interact with the AI either by typing or by speaking, and the assistant responds with both text and generated audio.

## 🛠️ Tech Stack
- **Frontend:** `Streamlit` & `Streamlit-option-menu`.
- **AI Engine:** `Google Generative AI` (Gemini 1.5 Flash / Pro).
- **Speech Features:** - `SpeechRecognition`: For converting Arabic/English voice to text.
  - `gTTS (Google Text-to-Speech)`: For vocalizing AI responses.
- **Directionality:** Custom CSS for **RTL (Right-to-Left)** support to accommodate Arabic users.

## 📊 Project Workflow
1. **API Authentication:** Users securely provide their Gemini API key via the sidebar.
2. **Input Selection:** Choose between **Keyboard** (Text) or **Microphone** (Voice) input.
3. **Processing:** The system sends the query to Gemini's latest models with built-in error handling for model availability.
4. **Feedback:** The AI generates a text response and an MP3 audio file for immediate playback.
5. **Session History:** Maintains a chat-like interface for the duration of the session.

## ⚙️ Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sarahalsamadi/Streamlit-AI-Assistant.git](https://github.com/sarahalsamadi/Streamlit-AI-Assistant.git)

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Run the App:**
   ```bash
   streamlit run chatbot_by_streamlit.py

## 📝 Key Features
- **Arabic First:** Full RTL layout and Arabic voice recognition support.
- **Voice-Enabled:** Integrated microphone support with ambient noise adjustment.
- **Model Fallback:** Smart logic that automatically tries different Gemini versions (1.5-flash, pro) to ensure connectivity.
- **Responsive UI:** Clean and minimal interface with horizontal navigation menus.
- **Secure API Handling:** API keys are entered via the UI and not hardcoded, following security best practices.
