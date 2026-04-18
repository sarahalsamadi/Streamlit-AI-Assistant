import speech_recognition as sr
from gtts import gTTS
import os
import google.generativeai as genai
from streamlit_option_menu import option_menu
import streamlit as st
import time

# --- 1. الإعدادات والواجهة | Setup & UI ---
st.set_page_config(page_title="AI Assistant 2026", layout="centered")

# دعم اللغة العربية | RTL Support
st.markdown("""<style> .stApp { direction: rtl; text-align: right; } .stChatMessage { direction: rtl; } </style>""", unsafe_allow_html=True)

with st.sidebar:
    st.title("⚙️ الإعدادات")
    # جعل المفتاح مدخلاً من المستخدم لضمان الأمان  
    user_api_key = st.text_input("أدخل مفتاح Gemini API الخاص بك:", type="password")
    if user_api_key:
        genai.configure(api_key=user_api_key)
    st.info("احصل على مفتاحك من: aistudio.google.com")

def get_ai_response(prompt):
    """دالة ذكية تحاول الاتصال بكل الموديلات الممكنة لتفادي الخطأ """
    # قائمة الموديلات بالترتيب (من الأحدث للأقدم)
    model_names = [
        'gemini-1.5-flash',
        'models/gemini-1.5-flash',
        'gemini-pro',
        'models/gemini-pro'
    ]
    
    success = False
    response_text = ""
    
    if not user_api_key:
        return "⚠️ يرجى إدخال مفتاح API في الشريط الجانبي أولاً."

    for name in model_names:
        try:
            model = genai.GenerativeModel(name)
            # إضافة تعليمات النظام لضمان التخصص في الذكاء الاصطناعي
            full_query = f"أنت خبير ذكاء اصطناعي. أجب باختصار: {prompt}"
            response = model.generate_content(full_query)
            response_text = response.text
            success = True
            break # إذا نجح موديل، نتوقف عن تجربة البقية
        except Exception:
            continue
            
    if success:
        return response_text
    else:
        return "❌ فشل الاتصال بكافة الموديلات. تأكد من صلاحية المفتاح أو جرب تحديث المكتبة عبر: pip install -U google-generativeai"

# --- 2. معالجة الصوت | Audio Engine ---
def speak(text):
    try:
        ts = int(time.time())
        filename = f"voice_{ts}.mp3"
        tts = gTTS(text=text, lang='ar')
        tts.save(filename)
        return filename
    except: return None

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.toast("👂 جاري الاستماع...")
        r.adjust_for_ambient_noise(source, duration=0.8)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            return r.recognize_google(audio, language="ar-SA")
        except: return ""

# --- 3. هيكل التطبيق | App Logic ---
if 'messages' not in st.session_state:
    st.session_state.messages = []

st.title("🤖 مساعد الذكاء الاصطناعي")

choice = option_menu(None, ["كتابة", "صوت"], icons=['pencil', 'mic'], orientation="horizontal")

user_msg = ""
if choice == "كتابة":
    user_msg = st.chat_input("اسأل خبير الـ AI...")
else:
    if st.button("🎤 اضغط للتحدث", use_container_width=True):
        user_msg = listen()

if user_msg:
    with st.spinner("🧠 جاري التفكير..."):
        ai_reply = get_ai_response(user_msg)
        audio_path = speak(ai_reply) if "❌" not in ai_reply else None
        st.session_state.messages.append({"q": user_msg, "a": ai_reply, "snd": audio_path})
    st.rerun()

# عرض المحادثة
for m in reversed(st.session_state.messages):
    with st.chat_message("user"): st.write(m["q"])
    with st.chat_message("assistant"):
        st.write(m["a"])
        if m["snd"] and os.path.exists(m["snd"]): st.audio(m["snd"])