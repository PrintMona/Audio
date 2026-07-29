import os
import whisper
import sounddevice as sd
import soundfile as sf
import cohere
from dotenv import load_dotenv
from RealtimeTTS import TextToAudioStream, SystemEngine

# ==========================
# Load API Key
# ==========================
load_dotenv()

api_key = os.getenv("COHERE_API_KEY")

if not api_key:
    print("COHERE_API_KEY not found!")
    exit()

co = cohere.Client(api_key)

# ==========================
# Load Whisper
# ==========================
print("Loading Whisper model...")
model = whisper.load_model("base")
print("Whisper loaded successfully!")

# ==========================
# Record Audio
# ==========================
duration = 10
sample_rate = 16000

# استخدمي رقم الميكروفون الذي نجح معك
sd.default.device = 1

print("\nSpeak now...")

audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="float32"
)

sd.wait()

sf.write("input.wav", audio, sample_rate)

print("Recording finished!")

# ==========================
# Speech to Text
# ==========================
result = model.transcribe("input.wav")

user_text = result["text"].strip()

print("\nYou said:")
print(user_text)

# إذا لم يلتقط أي كلام
if user_text == "":
    print("No speech detected.")
    exit()

# ==========================
# Cohere
# ==========================
response = co.chat(
    model="command-a-03-2025",
    message=user_text
)

ai_response = response.text

print("\nAI Response:")
print(ai_response)

# ==========================
# Text To Speech
# ==========================
engine = SystemEngine()

stream = TextToAudioStream(engine)

print("\nSpeaking...")

stream.feed(ai_response)
stream.play()

print("\nFinished!")